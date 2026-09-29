from openai import OpenAI

client = OpenAI()

print("\n🤖 JOB AI — создание профиля кандидата\n")

TEST_MODE = True

if TEST_MODE:
    candidate = {
        "name": "Ицхак",
        "profession": "Сварщик",
        "experience": "5",
        "city": "Ашкелон",
        "work_area": "Да, Ашдод",
        "skills": "Резка и сварка металла, электросварка и полуавтомат",
        "education": "Учился 3 года в техникуме, сварщик 2 разряда",
        "hebrew": "Начальный",
        "english": "Начальный",
        "languages": "Русский",
        "license": "Категория B",
        "salary": "10000",
        "extra": "Ответственный, люблю свою работу, готов учиться"
    }

else:
    name = input("Как тебя зовут? ")
    profession = input("Какая у тебя профессия? ")
    experience = input("Сколько лет опыта работы? ")
    city = input("В каком городе ты живёшь? ")
    work_area = input("Готов работать в других городах? Если да — где? ")
    skills = input("Расскажи, что ты умеешь делать по работе: ")
    education = input("Какое у тебя образование или профессиональная подготовка? ")
    hebrew = input("Какой у тебя уровень иврита? ")
    english = input("Какой у тебя уровень английского? ")
    languages = input("Какие ещё языки ты знаешь? ")
    license = input("Есть водительские права? Какие? ")
    salary = input("Какую зарплату ты хочешь получать? ")
    extra = input("Есть что-нибудь важное, что ты хочешь добавить? ")

    candidate = {
        "name": name,
        "profession": profession,
        "experience": experience,
        "city": city,
        "work_area": work_area,
        "skills": skills,
        "education": education,
        "hebrew": hebrew,
        "english": english,
        "languages": languages,
        "license": license,
        "salary": salary,
        "extra": extra
    }

print("\n" + "=" * 40)
print("ПРОФИЛЬ КАНДИДАТА")
print("=" * 40)

for key, value in candidate.items():
    print(f"{key}: {value}")

print("\n✅ Данные кандидата собраны.")
print("\n🤖 AI создаёт резюме на иврите...\n")

import json

prompt = f"""
Ты профессиональный специалист по составлению резюме для рынка труда Израиля.

На основе данных кандидата создай содержание профессионального резюме на иврите.

ВАЖНО:
- Используй только данные кандидата.
- Ничего не выдумывай.
- Не указывай желаемую зарплату.
- Пиши на профессиональном иврите.
- Верни ТОЛЬКО JSON.
- Не используй Markdown.
- Не используй ```json.
- Не добавляй никакого текста до или после JSON.

Формат:

{{
    "name": "имя на иврите",
    "profession": "профессия на иврите",
    "summary": "краткий профессиональный профиль",
    "experience": [
        "пункт опыта",
        "пункт опыта"
    ],
    "skills": [
        "навык",
        "навык"
    ],
    "education": "образование",
    "languages": [
        "язык и уровень"
    ],
    "license": "водительские права",
    "work_area": "предпочтительный регион работы"
}}

Данные кандидата:
{candidate}
"""

response = client.responses.create(
    model="gpt-5.6-luna",
    input=prompt
)

resume_data = json.loads(response.output_text)

print("\n✅ AI вернул структурированное резюме")
print(resume_data)

skills_html = "".join(
    f"<li>{skill}</li>"
    for skill in resume_data["skills"]
)

experience_html = "".join(
    f"<li>{item}</li>"
    for item in resume_data["experience"]
)

languages_html = "".join(
    f"<li>{language}</li>"
    for language in resume_data["languages"]
)

html = f"""
<!DOCTYPE html>
<html lang="he" dir="rtl">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>{resume_data["name"]} - קורות חיים</title>

    <style>
        body {{
            font-family: Arial, sans-serif;
            direction: rtl;
            text-align: right;
            background: #f5f5f5;
            margin: 0;
            padding: 40px 20px;
            color: #222;
        }}

        .resume {{
            max-width: 800px;
            margin: auto;
            background: white;
            padding: 50px;
            border-radius: 12px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        }}

        h1 {{
            margin-bottom: 5px;
            font-size: 36px;
        }}

        .profession {{
            font-size: 21px;
            color: #555;
            margin-bottom: 35px;
        }}

        h2 {{
            margin-top: 32px;
            padding-bottom: 8px;
            border-bottom: 1px solid #ddd;
            font-size: 22px;
        }}

        p, li {{
            font-size: 17px;
            line-height: 1.7;
        }}

        ul {{
            padding-right: 22px;
        }}

        .details {{
            line-height: 1.9;
        }}
    </style>
</head>

<body>

<div class="resume">

    <h1>{resume_data["name"]}</h1>
    <div class="profession">{resume_data["profession"]}</div>

    <h2>פרופיל מקצועי</h2>
    <p>{resume_data["summary"]}</p>

    <h2>ניסיון מקצועי</h2>
    <ul>
        {experience_html}
    </ul>

    <h2>מיומנויות</h2>
    <ul>
        {skills_html}
    </ul>

    <h2>השכלה והכשרה מקצועית</h2>
    <p>{resume_data["education"]}</p>

    <h2>שפות</h2>
    <ul>
        {languages_html}
    </ul>

    <h2>פרטים נוספים</h2>

    <div class="details">
        <div><strong>רישיון נהיגה:</strong> {resume_data["license"]}</div>
        <div><strong>אזור עבודה:</strong> {resume_data["work_area"]}</div>
    </div>

</div>

</body>
</html>
"""

with open("resume.html", "w", encoding="utf-8") as file:
    file.write(html)

print("\n✅ Новое резюме сохранено в resume.html")