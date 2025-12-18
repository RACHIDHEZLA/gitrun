# 🚀 gitrun

[![PyPI version](https://img.shields.io/pypi/v/gitrun.svg)](https://pypi.org/project/gitrun/)
[![Python versions](https://img.shields.io/pypi/pyversions/gitrun.svg)](https://pypi.org/project/gitrun/)
[![Downloads](https://img.shields.io/pypi/dm/gitrun.svg)](https://pypi.org/project/gitrun/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![GitHub stars](https://img.shields.io/github/stars/RACHIDHEZLA/gitrun?style=social)](https://github.com/RACHIDHEZLA/gitrun/stargazers)

**gitrun** هي أداة سطر أوامر بسيطة وقوية تمكنك من **تشغيل سكربتات بايثون مباشرة من مستودعات GitHub أو GitLab** بدون الحاجة لتنزيل المستودع كاملاً (git clone).

### ✨ المميزات الرئيسية
- 🚀 **تشغيل فوري** بدون clone
- 🛡️ **بيئة افتراضية معزولة تلقائياً** (لا تلوث بيئتك الحالية)
- 📦 **تثبيت تلقائي** للمتطلبات من `requirements.txt`
- 🔍 **اكتشاف تلقائي** للملف الرئيسي (main.py, app.py, cli.py …)
- 💾 **تخزين مؤقت ذكي** لتسريع التشغيل المتكرر
- 🧹 **تنظيف كامل** للملفات المؤقتة بعد الانتهاء
- 🌍 **دعم GitHub و GitLab**
- ✅ **تمرير arguments** كامل للسكربت الأصلي

## 📦 التثبيت

### الطريقة الموصى بها (خاصة على Ubuntu/Debian وتوزيعات حديثة)

```bash
sudo apt install pipx      # تثبيت pipx (مرة واحدة)
pipx ensurepath            # إضافة pipx إلى PATH (قد تحتاج إعادة فتح الطرفية)
pipx install gitrun
```

### الطريقة العادية

```bash
pip install gitrun
```

> **ملاحظة مهمة**: في التوزيعات الحديثة (مثل Ubuntu 23.04+ أو Debian 12+) قد يظهر خطأ `externally-managed-environment`. في هذه الحالة استخدم **pipx** (الحل الأمثل لأدوات CLI).

## 🎯 الاستخدام

### تشغيل أساسي (اكتشاف تلقائي للملف الرئيسي)

```bash
gitrun https://github.com/karpathy/micrograd
```

### تحديد سكربت معين

```bash
gitrun https://github.com/user/repo --script app.py
```

### تحديد فرع (branch)

```bash
gitrun https://github.com/user/repo --branch develop
```

### تمرير arguments للسكربت الأصلي

```bash
gitrun https://github.com/user/repo -- --input data.txt --output result.json
```

### تشغيل بدون بيئة افتراضية (استخدام البيئة الحالية)

```bash
gitrun https://github.com/user/repo --no-venv
```

### دعم GitLab

```bash
gitrun https://gitlab.com/user/project
```

### خيارات إضافية

```bash
gitrun --version                  # عرض الإصدار
gitrun --help                     # عرض المساعدة الكاملة
gitrun --verbose                  # عرض تفاصيل التشغيل (مفيد للتصحيح)
gitrun --clear-cache              # مسح التخزين المؤقت
```

## 📝 أمثلة عملية

```bash
# تجربة مشروع شهير بسرعة
gitrun https://github.com/karpathy/micrograd

# تشغيل أداة CLI مع arguments
gitrun https://github.com/pallets/click -- --help

# مشروع على GitLab
gitrun https://gitlab.com/torvalds/linux --script scripts/checkpatch.pl

# عرض تفاصيل التنفيذ
gitrun https://github.com/RACHIDHEZLA/gitrun --verbose
```

## 🔧 كيف تعمل gitrun؟

1. تحليل رابط المستودع (GitHub أو GitLab)
2. إنشاء مجلد وبيئة افتراضية مؤقتة
3. جلب وتثبيت `requirements.txt` (إن وجد)
4. اكتشاف وتنزيل السكربت الرئيسي
5. تشغيل السكربت مع الـ arguments المطلوبة
6. حذف كل الملفات المؤقتة تلقائياً

## 🤝 المساهمة

المساهمات مرحب بها جدًا! اقرأ [CONTRIBUTING.md](CONTRIBUTING.md) لمعرفة كيفية البدء.

## 📄 الرخصة

المشروع مرخص تحت رخصة [MIT](LICENSE).

---

**⭐ إذا أعجبتك الأداة، ضع نجمة على الريبو وشاركها مع أصدقائك!**  
https://github.com/RACHIDHEZLA/gitrun

شكرًا لتجربتك gitrun! 🚀
