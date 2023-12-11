<script>
    async function sendMessage() {
        const userInput = document.getElementById('user-input').value.trim();

        if (userInput !== '') {
            appendMessage('You', userInput, 'user-message');

            try {
                const response = await fetch('/chat', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/x-www-form-urlencoded',
                    },
                    body: 'user_input=' + encodeURIComponent(userInput),
                });

                if (response.ok) {
                    const { bot_response } = await response.json();
                    appendMessage('Chatbot', bot_response, 'bot-message');
                } else {
                    throw new Error(`Failed to get response: ${response.status}`);
                }
            } catch (error) {
                console.error('Error in getting response:', error.message);
            }
        }
    }
</script>

