document.addEventListener('DOMContentLoaded', async () => {
  try {
    const data = await (await fetch('https://swapi-api.hbtn.io/api/films/?format=json')).json();
    data.results.forEach(movie =>
      document.querySelector('#list_movies').appendChild(Object.assign(document.createElement('li'), { textContent: movie.title }))
    );
  } catch (error) {}
});
