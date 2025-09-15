from django.db import models

class GithubReport(models.Model):
    owner = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    stars = models.IntegerField()
    forks = models.IntegerField()
    watchers = models.IntegerField()
    is_fork = models.BooleanField()
    is_archived = models.BooleanField()
    languages = models.JSONField()
    language_count = models.IntegerField()
    topics = models.JSONField() 
    topic_count = models.IntegerField()
    disk_usage_kb = models.IntegerField()
    pull_requests = models.IntegerField()
    issues = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    primary_language = models.CharField(max_length=40, null=True, blank=True)
    created_at = models.DateTimeField()
    pushed_at = models.DateTimeField()
    default_branch_commit_count = models.IntegerField(null=True, blank=True)
    license = models.CharField(max_length=100, null=True, blank=True)
    assignable_user_count = models.IntegerField()
    code_of_conduct = models.CharField(max_length=100, null=True, blank=True)
    forking_allowed = models.BooleanField()
    name_with_owner = models.CharField(max_length=200)
    parent = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.nameWithOwner

#normalash uchun model
class GithubLanguage(models.Model):
    repo = models.ForeignKey(GithubReport, on_delete=models.CASCADE, related_name="repo_languages")
    name = models.CharField(max_length=100)
    size = models.BigIntegerField()
    year = models.IntegerField()

    class Meta:
        indexes = [
            models.Index(fields=['year', 'name']),
        ]