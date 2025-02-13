document.getElementById('chat-form').addEventListener('submit', function (e) {
    e.preventDefault(); // Предотвращаем перезагрузку страницы

    const userInput = document.getElementById('user-input');
    const messageText = userInput.value.trim();

    if (messageText === '') return;

    // Добавляем сообщение пользователя
    addMessage(messageText, 'user-message');

    // Очищаем поле ввода
    userInput.value = '';

    // Отправляем запрос к API
    fetch('/generate/', {  // Убедитесь, что URL заканчивается на "/"
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'  // Указываем формат данных
        },
        body: JSON.stringify({ prompt: messageText })  // Корректный формат данных
    })
    .then(response => {
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        return response.json();
    })
    .then(data => {
        addMessage(data.generated_text, 'bot-message');
    })
    .catch(error => {
        console.error('Ошибка при получении ответа:', error);
        addMessage('Извините, произошла ошибка.', 'bot-message');
    });
});

function addMessage(text, className) {
    const messagesDiv = document.getElementById('messages');
    // Создаём блок для сообщения
    const container = document.createElement('div');
    container.classList.add('message-container', className);
    container.textContent = text;
    messagesDiv.appendChild(container);

    // Прокручиваем окно чата вниз
    messagesDiv.scrollTop = messagesDiv.scrollHeight;
}

function getBotResponse(userMessage) {
    // Простейшая имитация ответа бота
    const responses = [
        "Это интересный вопрос!",
        "Я думаю, вам стоит изучить это подробнее.",
        "Попробуйте поискать информацию в учебниках.",
        "Я не уверен, но могу предположить, что это связано с вашим запросом."
    ];
    const randomIndex = Math.floor(Math.random() * responses.length);
    return responses[randomIndex];
}

