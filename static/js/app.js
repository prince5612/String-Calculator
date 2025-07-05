

let history = [];

document.getElementById('calculate').addEventListener('click', async () => {
  const expr = document.getElementById('expression').value.trim();
  const resEl = document.getElementById('result');
  const errEl = document.getElementById('error');
  errEl.textContent = '';

  try {
    const resp = await fetch('/api/calc', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ expression: expr })
    });
    const data = await resp.json();
    if (resp.ok) {
      resEl.textContent = data.result;
      addHistory(expr, data.result);
    } else {
      errEl.textContent = data.error;
      resEl.textContent = '';
    }
  } catch {
    errEl.textContent = 'Network error';
  }
});

// Copy only numeric result
document.getElementById('copy').addEventListener('click', () => {
  const value = document.getElementById('result').textContent;
  if (value) navigator.clipboard.writeText(value);
});

function addHistory(expr, res) {
  history.unshift({ expr, res });
  if (history.length > 10) history.pop();
  renderHistory();
}

function renderHistory() {
  const list = document.getElementById('historyList');
  list.innerHTML = '';
  history.forEach(item => {
    const li = document.createElement('li');
    li.textContent = `${item.expr} = ${item.res}`;
    list.appendChild(li);
  });
}

