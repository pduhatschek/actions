let html = ``
var requestURL = 'https://raw.githubusercontent.com/allisonsampaio/actions/master/data/users.json';
var request = new XMLHttpRequest();
request.open('GET', requestURL);
request.responseType = 'json';
request.send();

request.onload = function () {
    var users = request.response;
    for (u in users['users']) {
        html += `<div class="card border-left-info shadow h-100 py-2">
                  <div class="card-body">
                    <div class="row no-gutters align-items-center">
    
                      <div class="col mr-2">
                        <div class="text-xs font-weight-bold text-info text-uppercase mb-1">
                          ${users['users'][u]['login']}</div>
                        <div class="h5 mb-0 font-weight-bold text-gray-800">${users['users'][u]['event']['issue_comment']}</div>
                      </div>
                      <div class="col-auto">
                        <img class="img-profile rounded-circle"
                        src="${users['users'][u]['avatar_url']}"
                        style="height: 3rem; width: 3rem;">
                      </div>
    
                    </div>
                  </div>
                </div>`;
    }
    var target = document.getElementById('dashboard-points');
    var newElement = document.createElement('div');
    newElement.classList.add('col-xl-3', 'col-md-6', 'mb-4');
    newElement.innerHTML = html;
    target.parentElement.insertBefore(newElement, target.nextSibling);
}