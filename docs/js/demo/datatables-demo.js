// Call the dataTables jQuery plugin
$(document).ready(function() {
  $('#dataTable').DataTable();
});


// Definindo o caminho do arquivo JSON
const jsonPath = 'data/users.json';

// Obtendo a tabela
const tableBody = document.querySelector('#dataTable tbody');

// Função para preencher uma linha da tabela com os dados do usuário
function populateTableRow(user) {
  const row = tableBody.insertRow();

  const idCell = row.insertCell();
  idCell.innerText = user.id;

  const userCell = row.insertCell();
  userCell.innerText = user.login;
}

// Função para preencher a tabela com os dados dos usuários
function populateTable(data) {
  const users = data.users;
  users.forEach(user => {
    populateTableRow(user);
  });
}

// Função para carregar o arquivo JSON e preencher a tabela
function loadJsonAndPopulateTable(jsonPath) {
  fetch(jsonPath)
    .then(response => response.json())
    .then(data => {
      populateTable(data);
    })
    .catch(error => {
      console.error('Erro ao carregar o arquivo JSON:', error);
    });
}

// Chamando a função para carregar o arquivo JSON e preencher a tabela
loadJsonAndPopulateTable(jsonPath);

