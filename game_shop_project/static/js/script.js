// Переменная для хранения текущего индекса игры, который нужно загрузить
let currentIndex = 12;

const loadMoreGames = () => {
    const loadMoreButton = document.getElementById('load-more');
    const gamesGrid = document.getElementById('games-grid');

    console.log(`Загружаем игры с индексом от: ${currentIndex}`);

    fetch(`/load_more_games/?start=${currentIndex}`)  // Делаем запрос к серверу для получения новых игр
        .then(response => {
            console.log("Ответ от сервера получен");
            return response.json();
        })
        .then(data => {
            console.log('Данные с сервера:', data);

            // Добавляем новые игры в контейнер
            data.games.forEach(game => {
                const gameCard = document.createElement('div');
                gameCard.classList.add('game-card');
                gameCard.innerHTML = `
                    <img src="${game.image_url}" alt="${game.title}" class="game-image">
                    <div class="game-info">
                        <h3 class="game-title">${game.title}</h3>
                        <p class="game-price">$${game.price}</p>
                        <button class="btn-buy">Купить</button>
                    </div>
                `;
                gamesGrid.appendChild(gameCard);
            });

            // Обновляем текущий индекс
            currentIndex += data.games.length;

            // Если больше нет игр, скрываем кнопку "Показать еще"
            if (!data.has_more) {
                loadMoreButton.style.display = 'none';
                console.log("Больше нет игр для загрузки.");
            }
        })
        .catch(error => {
            console.error('Ошибка при загрузке:', error);
        });
};

// Обработчик клика по кнопке "Загрузить еще"
document.getElementById('load-more').addEventListener('click', loadMoreGames);
