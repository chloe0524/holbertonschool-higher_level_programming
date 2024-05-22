document.addEventListener('DOMContentLoaded', async () => {
  try {
    const response = await fetch('https://hellosalut.stefanbohacek.dev/?lang=fr');
    const data = await response.json();
    document.getElementById('hello').innerHTML = data.hello;
  } catch (error) {
    console.error('Error found => ', error);
  }
});
