document.addEventListener('DOMContentLoaded', () =>
  document.querySelector('#add_item').addEventListener('click', () =>
    document.querySelector('.my_list').appendChild(Object.assign(document.createElement('li'), { textContent: 'Item' }))
  )
);
