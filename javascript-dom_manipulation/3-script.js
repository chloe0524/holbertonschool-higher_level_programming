document.getElementById('toggle_header').onclick = () => {
  const header = document.querySelector('header');
  header.className = header.className === 'red' ? 'green' : 'red';
};
