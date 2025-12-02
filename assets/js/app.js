(function () {

  function getDbUrl() {
    return sessionStorage.getItem('dbUrl') || '';
  }

  function getToken() {
    return sessionStorage.getItem('dbToken') || '';
  }

  function authParam() {
    const t = getToken();
    return t ? `?auth=${encodeURIComponent(t)}` : '';
  }

  function apiPath(ref) {
    const url = getDbUrl();
    if (!url) throw new Error('Realtime Database URL não configurada. Faça login e informe a URL.');
    return `${url.replace(/\/+$/, '')}/${ref}.json`;
  }
  
  async function fetchJson(url, opts = {}) {
    const res = await fetch(url + authParam(), opts);
    
    if (!res.ok) {
      const text = await res.text();
      throw new Error(`Erro HTTP ${res.status}: ${text}`);
    }
    
    try {
        const contentType = res.headers.get("content-type");
        if (contentType && contentType.includes("application/json")) {
            return await res.json();
        }
        return null;
    } catch (e) {
        return null; 
    }
  }
  
  async function pacientes_listar() {
    const url = apiPath('pacientes');
    const data = await fetchJson(url);
    if (!data) return [];
    
    if (Array.isArray(data)) return data.filter(d => d && typeof d === 'object');
    
    return Object.keys(data).map(k => {
      const v = data[k];
      if (v && typeof v === 'object') v.cpf = v.cpf || k;
      return v;
    }).filter(Boolean); 
  }
  async function pacientes_criar(paciente) {
    const url = apiPath(`pacientes/${encodeURIComponent(paciente.cpf)}`);
    return fetchJson(url, { method: 'PUT', body: JSON.stringify(paciente) });
  }
  async function pacientes_atualizar(cpf, patch) {
    const url = apiPath(`pacientes/${encodeURIComponent(cpf)}`);
    return fetchJson(url, { method: 'PATCH', body: JSON.stringify(patch) });
  }
  async function pacientes_remover(cpf) {
    const url = apiPath(`pacientes/${encodeURIComponent(cpf)}`);
    return fetchJson(url, { method: 'DELETE' });
  }

  async function profissionais_listar() {
    const url = apiPath('profissionais');
    const data = await fetchJson(url);
    if (!data) return [];
    
    if (Array.isArray(data)) return data.filter(d => d && typeof d === 'object');
    
    return Object.keys(data).map(k => {
      const v = data[k];
      if (v && typeof v === 'object') v.crm = v.crm || k;
      return v;
    }).filter(Boolean);
  }
  async function profissionais_criar(prof) {
    const url = apiPath(`profissionais/${encodeURIComponent(prof.crm)}`);
    return fetchJson(url, { method: 'PUT', body: JSON.stringify(prof) });
  }
  async function profissionais_atualizar(crm, patch) {
    const url = apiPath(`profissionais/${encodeURIComponent(crm)}`);
    return fetchJson(url, { method: 'PATCH', body: JSON.stringify(patch) });
  }
  async function profissionais_remover(crm) {
    const url = apiPath(`profissionais/${encodeURIComponent(crm)}`);
    return fetchJson(url, { method: 'DELETE' });
  }

  async function medicamentos_listar() {
    const url = apiPath('medicamentos');
    const data = await fetchJson(url);
    if (!data) return [];
    
    if (Array.isArray(data)) return data.filter(d => d && typeof d === 'object');
    return Object.values(data).filter(v => v && typeof v === 'object');
  }
  async function medicamentos_criar(med) {
    const key = encodeURIComponent(med.nome.toLowerCase());
    const url = apiPath(`medicamentos/${key}`);
    return fetchJson(url, { method: 'PUT', body: JSON.stringify(med) });
  }
  async function medicamentos_atualizar(nomeKey, patch) {
    const url = apiPath(`medicamentos/${encodeURIComponent(nomeKey)}`);
    return fetchJson(url, { method: 'PATCH', body: JSON.stringify(patch) });
  }
  async function medicamentos_remover(nomeKey) {
    const url = apiPath(`medicamentos/${encodeURIComponent(nomeKey)}`);
    return fetchJson(url, { method: 'DELETE' });
  }

  async function pushResource(refName, obj) {
    const url = apiPath(refName);
    const res = await fetchJson(url, { method: 'POST', body: JSON.stringify(obj) });
    return res;
  }
  

  async function listarPush(refName) {
    const url = apiPath(refName);
    const data = await fetchJson(url);
    if (!data) return [];
    
    return Object.keys(data).map(k => {
      const v = data[k];
      if (v && typeof v === 'object') {
        v.id = v.id || k; 
        return v;
      }
      return null;
    }).filter(Boolean); 
  }

  async function atualizarPush(refName, id, patch) {
    const url = apiPath(`${refName}/${encodeURIComponent(id)}`);
    return fetchJson(url, { method: 'PATCH', body: JSON.stringify(patch) });
  }
  
  async function removerPush(refName, id) {
    const url = apiPath(`${refName}/${encodeURIComponent(id)}`);
    return fetchJson(url, { method: 'DELETE' });
  }

  function formatShort(item) {
    if (item.paciente && item.profissional) {
      return `${item.paciente.nome} (CPF: ${item.paciente.cpf}) com ${item.profissional.nome} (CRM: ${item.profissional.crm}) - Status: ${item.status || item.queixa}`;
    }
    if (item.paciente && item.tipo) {
      return `${item.tipo} para ${item.paciente.nome} (CPF: ${item.paciente.cpf}) - Status: ${item.status}`;
    }
    return JSON.stringify(item);
  }

  
  if (document.querySelector('.module')) {
    const dbInfo = document.getElementById('dbInfo');
    const moduleArea = document.getElementById('module-area');
    const modules = document.querySelectorAll('.module');

    function showDbInfo() {
      const url = getDbUrl() || '(não configurado)';
      dbInfo.textContent = `Realtime DB: ${url} — Token: ${getToken() ? '✓' : 'não informado'}`;
    }
    showDbInfo();

    modules.forEach(m => {
      m.addEventListener('click', () => openModule(m.dataset.module));
    });

    document.getElementById('logoutBtn').addEventListener('click', () => {
      sessionStorage.removeItem('dbUrl');
      sessionStorage.removeItem('dbToken');
      window.location.href = 'index.html'; 
    });

    function openModule(name) {
      moduleArea.innerHTML = ''; 
      
      const title = document.createElement('h3');
      title.textContent = `Gerenciar: ${name.charAt(0).toUpperCase() + name.slice(1)}`;
      moduleArea.appendChild(title);

      const controls = document.createElement('div');
      controls.className = 'module-controls';
      moduleArea.appendChild(controls);

      const form = document.createElement('form');
      form.className = 'module-form';
      form.onsubmit = e => e.preventDefault();
      moduleArea.appendChild(form);

      const listContainer = document.createElement('div');
      listContainer.className = 'module-list';
      moduleArea.appendChild(listContainer);

      if (name === 'pacientes') {
        form.innerHTML = `
          <label>Nome <input name="nome" required></label>
          <label>CPF (11 dígitos) <input name="cpf" required></label>
          <label>Data de nascimento <input name="nasc" placeholder="dd/mm/aaaa"></label>
          <button class="btn btn-primary" type="button" id="criar">Criar paciente</button>
        `;
        
        form.querySelector('#criar').addEventListener('click', async () => {
          const nome = form.nome.value.trim();
          const cpf = form.cpf.value.trim();
          if (!nome || !cpf) return alert('Nome e CPF são obrigatórios.');
          try {
            await pacientes_criar({ nome, cpf, nasc: form.nasc.value.trim() });
            alert('Paciente criado.');
            renderList();
          } catch (err) { alert('Erro: ' + err.message); }
        });

        async function renderList() {
          listContainer.innerHTML = '<p class="muted">Carregando...</p>';
          try {
            const lista = await pacientes_listar();
            if (!lista.length) { listContainer.innerHTML = '<p class="muted">Nenhum paciente.</p>'; return; }
            
            const ul = document.createElement('ul');
            lista.forEach(p => {
              const li = document.createElement('li');
              li.innerHTML = `<strong>${p.nome}</strong> — CPF: ${p.cpf} — Nasc: ${p.nasc || '-'}
                <button data-cpf="${p.cpf}" class="btn editar">Editar</button>
                <button data-cpf="${p.cpf}" class="btn remover">Remover</button>`;
              ul.appendChild(li);
            });
            listContainer.innerHTML = '';
            listContainer.appendChild(ul);

            listContainer.querySelectorAll('.remover').forEach(b => {
              b.addEventListener('click', async () => {
                const cpf = b.dataset.cpf;
                if (!confirm('Remover paciente ' + cpf + '?')) return;
                try { await pacientes_remover(cpf); alert('Removido.'); renderList(); } catch (err) { alert(err.message); }
              });
            });
            
            listContainer.querySelectorAll('.editar').forEach(b => {
              b.addEventListener('click', async () => {
                const cpf = b.dataset.cpf;
                const novoNome = prompt('Novo nome (em branco = sem alteração):');
                const novaNasc = prompt('Nova data de nascimento (em branco = sem alteração):');
                const patch = {};
                if (novoNome) patch.nome = novoNome;
                if (novaNasc) patch.nasc = novaNasc;
                if (Object.keys(patch).length === 0) return;
                try { await pacientes_atualizar(cpf, patch); alert('Atualizado.'); renderList(); } catch (err) { alert(err.message); }
              });
            });
          } catch (err) { listContainer.innerHTML = '<p class="muted">Erro: ' + err.message + '</p>'; }
        }
        
        renderList();
        return;
      }

      if (name === 'profissionais') {
        form.innerHTML = `
          <label>Nome <input name="nome" required></label>
          <label>Especialidade <input name="especialidade"></label>
          <label>CRM (número) <input name="crm" required></label>
          <button class="btn btn-primary" type="button" id="criar">Criar profissional</button>
        `;
        
        form.querySelector('#criar').addEventListener('click', async () => {
          const nome = form.nome.value.trim();
          const crm = form.crm.value.trim();
          if (!nome || !crm) return alert('Nome e CRM são obrigatórios.');
          try {
            await profissionais_criar({ nome, especialidade: form.especialidade.value.trim(), crm });
            alert('Profissional criado.');
            renderList();
          } catch (err) { alert(err.message); }
        });

        async function renderList() {
          listContainer.innerHTML = '<p class="muted">Carregando...</p>';
          try {
            const lista = await profissionais_listar();
            if (!lista.length) { listContainer.innerHTML = '<p class="muted">Nenhum profissional.</p>'; return; }
            
            const ul = document.createElement('ul');
            lista.forEach(p => {
              const li = document.createElement('li');
              li.innerHTML = `<strong>${p.nome}</strong> — CRM: ${p.crm} — ${p.especialidade || '-'}
                <button data-crm="${p.crm}" class="btn editar">Editar</button>
                <button data-crm="${p.crm}" class="btn remover">Remover</button>`;
              ul.appendChild(li);
            });
            listContainer.innerHTML = '';
            listContainer.appendChild(ul);

            listContainer.querySelectorAll('.remover').forEach(b => {
              b.addEventListener('click', async () => {
                const crm = b.dataset.crm;
                if (!confirm('Remover profissional ' + crm + '?')) return;
                try { await profissionais_remover(crm); alert('Removido.'); renderList(); } catch (err) { alert(err.message); }
              });
            });
            
            listContainer.querySelectorAll('.editar').forEach(b => {
              b.addEventListener('click', async () => {
                const crm = b.dataset.crm;
                const novoNome = prompt('Novo nome (em branco = sem alteração):');
                const novaEsp = prompt('Nova especialidade (em branco = sem alteração):');
                const patch = {};
                if (novoNome) patch.nome = novoNome;
                if (novaEsp) patch.especialidade = novaEsp;
                if (Object.keys(patch).length === 0) return;
                try { await profissionais_atualizar(crm, patch); alert('Atualizado.'); renderList(); } catch (err) { alert(err.message); }
              });
            });
          } catch (err) { listContainer.innerHTML = '<p class="muted">Erro: ' + err.message + '</p>'; }
        }
        
        renderList();
        return;
      }

      if (name === 'medicamentos') {
        form.innerHTML = `
          <label>Nome do medicamento <input name="nome" required></label>
          <label>Tarja (B,A,V,P) <input name="tarja" required></label>
          <button class="btn btn-primary" type="button" id="criar">Criar medicamento</button>
        `;
        
        form.querySelector('#criar').addEventListener('click', async () => {
          const nome = form.nome.value.trim();
          const tarja = form.tarja.value.trim().toLowerCase();
          if (!nome || !tarja) return alert('Preencha todos os campos.');
          if (!['b','a','v','p'].includes(tarja)) return alert('Tarja inválida. Use B, A, V ou P.');
          try {
            await medicamentos_criar({ nome: nome.toLowerCase(), tarja }); // Salva com nome em minúsculo
            alert('Medicamento criado.');
            renderList();
          } catch (err) { alert(err.message); }
        });

        async function renderList() {
          listContainer.innerHTML = '<p class="muted">Carregando...</p>';
          try {
            const lista = await medicamentos_listar();
            if (!lista.length) { listContainer.innerHTML = '<p class="muted">Nenhum medicamento.</p>'; return; }
            
            const ul = document.createElement('ul');
            lista.forEach(m => {
              const li = document.createElement('li');
              const tarjaFull = {b:'Branca',a:'Amarela',v:'Vermelha',p:'Preta'}[m.tarja] || m.tarja;
              li.innerHTML = `<strong>${m.nome}</strong> — Tarja: ${tarjaFull}
                <button data-key="${m.nome}" class="btn editar">Editar</button>
                <button data-key="${m.nome}" class="btn remover">Remover</button>`;
              ul.appendChild(li);
            });
            listContainer.innerHTML = '';
            listContainer.appendChild(ul);

            listContainer.querySelectorAll('.remover').forEach(b => {
              b.addEventListener('click', async () => {
                const key = b.dataset.key;
                if (!confirm('Remover medicamento ' + key + '?')) return;
                try { await medicamentos_remover(key); alert('Removido.'); renderList(); } catch (err) { alert(err.message); }
              });
            });
            
            listContainer.querySelectorAll('.editar').forEach(b => {
              b.addEventListener('click', async () => {
                const key = b.dataset.key;
                const novoTarja = prompt('Nova tarja (B/A/V/P):');
                if (!novoTarja) return;
                const code = novoTarja.trim().toLowerCase();
                if (!['b','a','v','p'].includes(code)) return alert('Tarja inválida.');
                try { await medicamentos_atualizar(key, { tarja: code }); alert('Atualizado.'); renderList(); } catch (err) { alert(err.message); }
              });
            });
          } catch (err) { listContainer.innerHTML = '<p class="muted">Erro: ' + err.message + '</p>'; }
        }
        
        renderList();
        return;
      }

      if (['exames','consultas','prontuarios'].includes(name)) {
        form.innerHTML = '';
        
        if (name === 'exames') {
          form.innerHTML = `
            <label>CPF do paciente <input name="cpf" required></label>
            <label>Tipo de exame <input name="tipo" required></label>
            <button class="btn btn-primary" id="criar">Solicitar exame</button>
          `;
          
          form.querySelector('#criar').addEventListener('click', async () => {
            const cpf = form.cpf.value.trim();
            const tipo = form.tipo.value.trim();
            if (!cpf || !tipo) return alert('Preencha os campos.');
            try {
              const pacList = await pacientes_listar();
              const pac = pacList.find(p => p.cpf === cpf);
              if (!pac) return alert('Paciente não encontrado.');
              
              const exame = {
                paciente: { nome: pac.nome, cpf: pac.cpf },
                tipo,
                resultado: 'Pendente',
                status: 'Solicitado',
                dataSolicitacao: new Date().toLocaleString()
              };
              const res = await pushResource('exames', exame);
              alert('Exame solicitado. ID: ' + (res.name || '—'));
              renderList();
            } catch (err) { alert(err.message); }
          });
        }

        if (name === 'consultas') {
          form.innerHTML = `
            <label>CPF do paciente <input name="cpf" required></label>
            <label>CRM do profissional <input name="crm" required></label>
            <label>Data (dd/mm/aaaa) <input name="data" required></label>
            <label>Hora (hh:mm) <input name="hora" required></label>
            <button class="btn btn-primary" id="criar">Agendar consulta</button>
          `;
          
          form.querySelector('#criar').addEventListener('click', async () => {
            const cpf = form.cpf.value.trim();
            const crm = form.crm.value.trim();
            try {
              const pac = (await pacientes_listar()).find(p => p.cpf === cpf);
              const prof = (await profissionais_listar()).find(p => p.crm === crm);
              if (!pac) return alert('Paciente não encontrado.');
              if (!prof) return alert('Profissional não encontrado.');
              
              const consulta = {
                paciente: { nome: pac.nome, cpf: pac.cpf },
                profissional: { nome: prof.nome, crm: prof.crm },
                data: form.data.value.trim(),
                hora: form.hora.value.trim(),
                status: 'Agendada'
              };
              const res = await pushResource('consultas', consulta);
              alert('Consulta criada. ID: ' + (res.name || '—'));
              renderList();
            } catch (err) { alert(err.message); }
          });
        }

        if (name === 'prontuarios') {
          form.innerHTML = `
            <label>CPF do paciente <input name="cpf" required></label>
            <label>CRM do profissional <input name="crm" required></label>
            <label>Queixa principal <input name="queixa" required></label>
            <label>Diagnóstico / Observações <input name="diagnostico"></label>
            <label>Prescrição <input name="prescricao"></label>
            <button class="btn btn-primary" id="criar">Registrar atendimento</button>
          `;
          
          form.querySelector('#criar').addEventListener('click', async () => {
            try {
              const cpf = form.cpf.value.trim();
              const crm = form.crm.value.trim();
              const pac = (await pacientes_listar()).find(p => p.cpf === cpf);
              const prof = (await profissionais_listar()).find(p => p.crm === crm);
              if (!pac) return alert('Paciente não encontrado.');
              if (!prof) return alert('Profissional não encontrado.');
              
              const registro = {
                paciente: { nome: pac.nome, cpf: pac.cpf },
                profissional: { nome: prof.nome, crm: prof.crm },
                queixa: form.queixa.value.trim(),
                diagnostico: form.diagnostico.value.trim(),
                prescricao: form.prescricao.value.trim(),
                data: new Date().toLocaleString(),
              };
              const res = await pushResource('prontuarios', registro);
              alert('Prontuário registrado. ID: ' + (res.name || '—'));
              renderList();
            } catch (err) { alert(err.message); }
          });
        }

        async function renderList() {
          listContainer.innerHTML = '<p class="muted">Carregando...</p>';
          try {
            const lista = await listarPush(name);
            if (!lista.length) { listContainer.innerHTML = `<p class="muted">Nenhum registro em ${name}.</p>`; return; }
            
            const ul = document.createElement('ul');
            lista.forEach(it => {
              const li = document.createElement('li');
              li.innerHTML = `<strong>ID: ${it.id || '(sem id)'}</strong> — ${formatShort(it)}
                <button data-id="${it.id}" class="btn editar">Editar</button>
                <button data-id="${it.id}" class="btn remover">Remover</button>`;
              ul.appendChild(li);
            });
            listContainer.innerHTML = '';
            listContainer.appendChild(ul);

            listContainer.querySelectorAll('.remover').forEach(b => {
              b.addEventListener('click', async () => {
                const id = b.dataset.id;
                if (!confirm('Remover registro ' + id + '?')) return;
                try { await removerPush(name, id); alert('Removido.'); renderList(); } catch (err) { alert(err.message); }
              });
            });

           listContainer.querySelectorAll('.editar').forEach(b => {
              b.addEventListener('click', async () => {
                const id = b.dataset.id;
                const novo = prompt('Campo JSON para patch (ex: {"status":"Concluido"}):');
                if (!novo) return;
                try {
                  const patch = JSON.parse(novo);
                  await atualizarPush(name, id, patch);
                  alert('Atualizado.'); renderList();
                } catch (err) { alert('Erro: ' + err.message); }
              });
            });

          } catch (err) { listContainer.innerHTML = '<p class="muted">Erro: ' + err.message + '</p>'; }
        }
        
        renderList();
        return;
      }

      moduleArea.innerHTML = '<p class="muted">Módulo não implementado.</p>';
    } 
  } 
  
})();