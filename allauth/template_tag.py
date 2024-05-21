<!-- templates/account/login.html -->

{% load socialaccount %}
{% load i18n %}

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Login</title>
</head>
<body>
    <h1>{% trans "Login" %}</h1>

    <form method="post" action="{% url 'account_login' %}">
        {% csrf_token %}
        {{ form.as_p }}
        <button type="submit">{% trans "Log In" %}</button>
    </form>

    <h2>{% trans "Or login with" %}</h2>
    <ul>
        {% providers_media_js %}
        {% for provider in socialaccount_providers %}
            <li><a href="{% provider_login_url provider.id %}">{{ provider.name }}</a></li>
        {% endfor %}
    </ul>

    <p><a href="{% url 'account_reset_password' %}">{% trans "Forgot Password?" %}</a></p>
    <p><a href="{% url 'account_signup' %}">{% trans "Sign Up" %}</a></p>
</body>
</html>

