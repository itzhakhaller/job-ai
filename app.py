from flask import Flask, request
from openai import OpenAI

app = Flask(__name__)
client = OpenAI()


@app.route("/", methods=["GET", "POST"])
def home():

        if request.method == "POST":
            name = request.form.get("name")
            last_name = request.form.get("last_name")
            name_he = request.form.get("name_he")
            age = request.form.get("age")
            phone = request.form.get("phone")
            email = request.form.get("email")
            city = request.form.get("city")
            profession = request.form.get("profession")
            experience = request.form.get("experience")
            skills = request.form.get("skills")
            education = request.form.get("education")
            hebrew = request.form.get("hebrew")
            english = request.form.get("english")
            languages = request.form.get("languages")
            driver_license = request.form.get("driver_license")
            work_area = request.form.get("work_area")
            salary = request.form.get("salary")
            additional_info = request.form.get("additional_info")

            print("Имя:", name)
            print("Фамилия:", last_name)
            print("Имя на иврите:", name_he)
            print("Возраст:", age)
            print("Телефон:", phone)
            print("Email:", email)
            print("Город:", city)
            print("Профессия:", profession)
            print("Опыт:", experience)
            print("Навыки:", skills)
            print("Образование:", education)
            print("Иврит:", hebrew)
            print("Английский:", english)
            print("Другие языки:", languages)
            print("Водительские права:", driver_license)
            print("Желаемая зарплата:", salary)
            print("Готовность работать в других городах:", work_area)
            print("Дополнительная информация:", additional_info)
            prompt = f"""
Создай профессиональное резюме на иврите.

Используй только информацию, которую предоставил пользователь.
Не придумывай опыт работы, навыки, образование, сертификаты,
места работы, должности, даты или другие факты.
Ты можешь улучшать формулировки и делать их профессиональными,
но не изменяй смысл предоставленной информации.
Если информации для какого-либо раздела недостаточно — не выдумывай её.
Не указывай желаемую зарплату в резюме.
Не добавляй личные качества кандидата, если пользователь сам их не указал.
Не делай предположений на основе профессии или опыта.
Используй имя на иврите в заголовке резюме точно так, как его ввёл пользователь.
Не переводи и не изменяй имя на иврите.

Имя: {name}
Фамилия: {last_name}
Имя на иврите: {name_he}
Возраст: {age}
Телефон: {phone}
Email: {email}
Город: {city}
Профессия: {profession}
Опыт работы: {experience} лет
Навыки: {skills}
Образование / специальность: {education}
Уровень иврита: {hebrew}
Уровень английского: {english}
Другие языки: {languages}
Водительские права: {driver_license}
Готовность работать в других городах: {work_area}
Желаемая зарплата: {salary} ₪ в месяц
Дополнительная информация: {additional_info}

Верни резюме на иврите в формате HTML.
Используй только теги <h1>, <h2>, <p>, <ul>, <li>.
Не используй Markdown и не пиши ```html.
"""
            response = client.responses.create(
                model="gpt-5.6-luna",
                input=prompt
            )

            resume = response.output_text

            print("\n🤖 AI СОЗДАЛ РЕЗЮМЕ:")
            print(resume)
            return f"""
            <!DOCTYPE html>
            <html lang="he" dir="rtl">

            <head>
                <meta charset="UTF-8">

                <style>
                    body {{
                        background: #f3f4f6;
                        font-family: Arial, sans-serif;
                        margin: 0;
                        padding: 40px;
                    }}

                    .resume {{
                        background: white;
                        max-width: 800px;
                        margin: auto;
                        padding: 50px;
                        border-radius: 12px;
                        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.10);
                    }}

                    .resume h1 {{
                        font-size: 32px;
                        margin-bottom: 8px;
                    }}

                    .resume h2 {{
                        font-size: 20px;
                        border-bottom: 2px solid #e5e7eb;
                        padding-bottom: 8px;
                        margin-top: 28px;
                    }}

                    .resume p,
                    .resume li {{
                        font-size: 16px;
                        line-height: 1.6;
                    }}
                </style>
            </head>

            <body>

                <div class="resume">
                    {resume}
                </div>

                <button onclick="window.print()">Скачать резюме / הורדת קורות חיים</button>

            </body>
            </html>
            """

        return """
    <!DOCTYPE html>
    <html lang="ru">
    <head>
        <meta charset="UTF-8">
        <title>Job AI</title>

        <style>
            body {
                background: #f3f4f6;
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 40px;
            }

            .form-container {
                background: white;
                max-width: 700px;
                margin: auto;
                padding: 40px;
                border-radius: 12px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.10);
            }

            input,
            textarea,
            select {
                width: 100%;
                padding: 12px;
                margin-top: 6px;
                box-sizing: border-box;
                border: 1px solid #d1d5db;
                border-radius: 8px;
                font-size: 16px;
            }

            button {
                width: 100%;
                padding: 14px;
                background: #2563eb;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
            }

            button:hover {
                background: #1d4ed8;
            }
        </style>
    </head>

    <body>
    
    <div class="form-container">

        <h1>🤖 JOB AI</h1>
        <h2>Резюме для работы в Израиле</h2>

        <p>
            Расскажите о себе — искусственный интеллект
            поможет создать профессиональное резюме на иврите.
        </p>

        <form method="POST">

    <label>Как вас зовут?</label>
    <br>

    <input type="text" name="name">

    <br><br>

<label>Ваша фамилия?</label>
<br>
<input type="text" name="last_name">

<br><br>

<label>Имя и фамилия на иврите</label>
<br>
<input type="text" name="name_he" dir="rtl">

<br><br>

<label>Сколько вам лет?</label>
<br>
<input type="number" name="age">

<br><br>

<label>Ваш номер телефона?</label>
<br>
<input type="tel" name="phone">

<br><br>

<label>Ваш Email?</label>
<br>
<input type="email" name="email">

<br><br>

<label>В каком городе вы живёте?</label>
<br>
<input type="text" name="city">

<br><br>

<label>Какая у вас профессия?</label>
<br>

<input type="text" name="profession">

<br><br>

<label>Сколько лет опыта работы?</label>
<br>
<input type="text" name="experience">

<br><br>

<label>Какие у вас профессиональные навыки?</label><br>
<input type="text" name="skills" required>

<br><br>

<label>Какое у вас образование или специальность?</label>
<br>
<input type="text" name="education">

<br><br>

<label>Какой у вас уровень иврита?</label>
<br>

<select name="hebrew">
    <option value="">Выберите уровень</option>
    <option value="Нет">Нет</option>
    <option value="Начальный">Начальный</option>
    <option value="Средний">Средний</option>
    <option value="Хороший">Хороший</option>
    <option value="Свободный">Свободный</option>
</select>

<br><br>

<label>Какой у вас уровень английского?</label>
<br>

<select name="english">
    <option value="">Выберите уровень</option>
    <option value="Нет">Нет</option>
    <option value="Начальный">Начальный</option>
    <option value="Средний">Средний</option>
    <option value="Хороший">Хороший</option>
    <option value="Свободный">Свободный</option>
</select>

<br><br>

<label>Какие ещё языки вы знаете?</label>
<br>
<input type="text" name="languages">

<br><br>

<label>Какие у вас водительские права?</label>
<br>

<select name="driver_license">
    <option value="">Выберите категорию</option>
    <option value="Нет">Нет водительских прав</option>
    <option value="A">A — мотоцикл</option>
    <option value="A1">A1 — мотоцикл</option>
    <option value="A2">A2 — мотоцикл</option>
    <option value="B">B — легковой автомобиль</option>
    <option value="C1">C1 — грузовой автомобиль</option>
    <option value="C">C — грузовой автомобиль</option>
</select>

<br><br>

<label>Готовы ли вы работать в других городах?</label>
<br>

<select name="work_area">
    <option value="">Выберите ответ</option>
    <option value="Да">Да</option>
    <option value="Нет">Нет</option>
</select>

<br><br>

<label>Какую зарплату вы хотите получать в месяц? (₪)</label>
<br>
<input type="number" name="salary">

<br><br>

<label>Что ещё вы хотели бы рассказать о себе?</label>
<br>
<textarea name="additional_info" rows="4" cols="40"></textarea>

<br><br>

<button type="submit">Создать резюме 🚀</button>

</form>

</div>

    </body>
    </html>
    """


if __name__ == "__main__":
    app.run(debug=True)