import json
from django.db import transaction
from django.utils.dateparse import parse_datetime
from django.core.management.base import BaseCommand

from reportapp.models import GithubReport, GithubLanguage


class Command(BaseCommand):
    help = "JSON fayldan GitHub repo va tillarni import qilish"

    def add_arguments(self, parser):
        parser.add_argument("file_path", type=str)

    @transaction.atomic
    def handle(self, *args, **options):
        file_path = options["file_path"]

        with open(file_path, "r") as f:
            data = json.load(f)

        report_objs = []
        language_objs = []

        for item in data:
            repo = GithubReport(
                owner=item.get("owner"),
                name=item.get("name"),
                stars=item.get("stars", 0),
                forks=item.get("forks", 0),
                watchers=item.get("watchers", 0),
                is_fork=item.get("isFork", False),
                is_archived=item.get("isArchived", False),
                languages=item.get("languages", []),
                language_count=item.get("languageCount", 0),
                topics=item.get("topics", []),
                topic_count=item.get("topicCount", 0),
                disk_usage_kb=item.get("diskUsageKb", 0),
                pull_requests=item.get("pullRequests", 0),
                issues=item.get("issues", 0),
                description=item.get("description"),
                primary_language=item.get("primaryLanguage"),
                created_at=parse_datetime(item.get("createdAt")),
                pushed_at=parse_datetime(item.get("pushedAt")),
                default_branch_commit_count=item.get("defaultBranchCommitCount"),
                license=item.get("license"),
                assignable_user_count=item.get("assignableUserCount", 0),
                code_of_conduct=item.get("codeOfConduct"),
                forking_allowed=item.get("forkingAllowed", False),
                name_with_owner=item.get("nameWithOwner"),
                parent=item.get("parent"),
            )
            report_objs.append(repo)

        GithubReport.objects.bulk_create(report_objs, batch_size=5000, ignore_conflicts=True)

        repo_map = {r.name_with_owner: r for r in GithubReport.objects.filter(
            name_with_owner__in=[x.name_with_owner for x in report_objs]
        )}

        # GithubLanguage ga normalash uchun bulk insert
        for item in data:
            repo = repo_map.get(item.get("nameWithOwner"))
            if not repo:
                continue
            year = parse_datetime(item.get("createdAt")).year
            for lang in item.get("languages", []):
                language_objs.append(
                    GithubLanguage(
                        repo=repo,
                        name=lang["name"],
                        size=lang["size"],
                        year=year,
                    )
                )

        GithubLanguage.objects.bulk_create(language_objs, batch_size=5000)

        self.stdout.write(
            self.style.SUCCESS(
                f"{len(report_objs)} ta repo va {len(language_objs)} ta tillar import qilindi"
            )
        )
