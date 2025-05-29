<!DOCTYPE html>
<html>

<head>
    <title>Резюме {{ resume.name }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
        }

        h1 {
            color: #333;
        }

        .section {
            margin-bottom: 20px;
        }

        .skills {
            display: flex;
            gap: 10px;
        }

        .skill {
            background: #eee;
            padding: 5px 10px;
            border-radius: 3px;
        }
    </style>
</head>

<body>
    <h1>{{ resume.name }}</h1>
    <h2>{{ resume.job }}</h2>

    <div class="section">
        <h3>О себе:</h3>
        <p>{{ resume.about }}</p>
    </div>

    <div class="section">
        <h3>Навыки:</h3>
        <div class="skills">
            {% for skill in resume.skills %}
            <div class="skill">{{ skill }}</div>
            {% endfor %}
        </div>
    </div>
</body>

</html>