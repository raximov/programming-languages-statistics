# Programming Languages Statistics

Berilgan JSON fayldagi GitHub repository metadata obyektlarini Django bazasiga import
qilishva REST API orqali statistik hisobot (report) chiqarish.
Yaratilgan repozitariyalardan eng ko'p dasturlash tili qo'llanilganlarini (top 5) yillar kesimida
chiqarish
---

## 📦 O‘rnatish

```bash
git clone https://github.com/raximov/programming-languages-statistics.git
cd programming-languages-statistics
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
```
---

## 🖥️ Migratsiya qilish

```bash
python manage.py makemigrations
python manage.py migrate
```
---

## ⚙️ Ma’lumotlarni import qilish

Loyiha `reportapp` ichida maxsus Django management command bilan keladi. JSON fayldan ma’lumotlarni import qilish uchun:

```bash
python manage.py importcode path/to/part1_1.json
```



✅ Ushbu buyruq:
- `GithubReport` jadvalini to‘ldiradi  
- Har bir repositoriyaning `languages` massivini **`GithubLanguage`** jadvaliga yozadi
- Shu orqali biz normalashda performanceni yaxshilashimiz mumkin



---

## 🗄️ Model tuzilmasi

**GithubReport** — asosiy repository ma’lumotlari:  
- owner, name, stars, forks, watchers  
- languages (JSON)  
- topics (JSON)  
- created_at, pushed_at va boshqa statistikalar  

**GithubLanguage** — har bir repository bo‘yicha dasturlash tillari:  
- repo (ForeignKey → GithubReport)  
- name (til nomi)  
- size (baytlarda hajm)  
- year (repo yaratilgan yili)  

---

## 🚀 API

### 1. Top 5 tillar bo‘yicha statistikasi
**Endpoint:**  
```
GET /api/report-orm/
```

**Namuna natija:**
```json
[
  {
		"year": 2025,
		"name": "C",
		"total_size": 2150560,
		"rownum": 4
	},
	{
		"year": 2025,
		"name": "TypeScript",
		"total_size": 1532749,
		"rownum": 5
	}
]
```

Bu API har bir yil bo‘yicha **eng ko‘p ishlatilgan TOP-5 dasturlash tillarini** qaytaradi.

---

## 🖥️ Serverni ishga tushirish

```bash
python manage.py runserver
```

Brauzer orqali oching:  
👉 `http://127.0.0.1:8000/`






- GitHub: [raximov](https://github.com/raximov)  
- Joylashuv: Buxoro  
