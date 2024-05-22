document.addEventListener('DOMContentLoaded', async () => {
  try {
    const response = await fetch('https://swapi-api.hbtn.io/api/people/5/?format=json');
    const data = await response.json();
    document.querySelector('#character').textContent = data.name;
  } catch (error) {
    console.error('Error fetching character:', error);
  }
});
