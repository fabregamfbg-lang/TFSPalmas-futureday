function createFutureDayForm() {
  const form = FormApp.create('Pré-Inscrição Future Day');
  
  // Configurações do formulário
  form.setDescription(`
*Pré-Inscrição Future Day**
Falta pouco para o grande dia! 🥳
A inauguração da The Future School está chegando, e você e seu filho estão oficialmente convidados.
Esse não vai ser um evento qualquer. Vai ser a chance do seu filho colocar a mão na massa de verdade e
viver um pouquinho do que é aprender por aqui.

**No dia, os alunos irão:**
🤖 Aprender a criar mecanismos automatizados no Minecraft;
👾 Dar os primeiros passos na programação dentro do Roblox;
🏆 Concorrer a prêmios especiais durante o evento!

**E tem mais:** quem estiver presente garante acesso aos nossos descontos de fundador, uma condição
exclusiva para as primeiras famílias que entrarem nessa história com a gente

**Endereço:** R. Visc. de Taunay, 902 - Sl 06 - Atiradores, Joinville

**AS INSCRIÇÕES OFICIAIS SERÃO REALIZADAS 2 DIAS ANTES DO EVENTO**

☁️
  `);
  
  form.setCollectEmail(false)
      .setLimitOneResponsePerUser(false)
      .setShowLinkToRespondAgain(false)
      .setAcceptingResponses(true);

  // Pergunta 1: Nome completo do responsável
  form.addTextItem()
      .setTitle('Qual o seu nome completo? *')
      .setRequired(true);

  // Pergunta 2: Data de nascimento do responsável
  form.addDateItem()
      .setTitle('Qual sua data de nascimento? *')
      .setRequired(true);

  // Pergunta 3: Endereço
  form.addTextItem()
      .setTitle('Qual seu endereço? *')
      .setRequired(true);

  // Pergunta 4: Telefone do responsável
  form.addTextItem()
      .setTitle('Qual seu telefone/WhatsApp? *')
      .setRequired(true);

  // Pergunta 5: Nome do filho
  form.addTextItem()
      .setTitle('Qual o nome do seu filho? *')
      .setRequired(true);

  // Pergunta 5: Data de nascimento do filho
  form.addDateItem()
      .setTitle('Qual a data de nascimento do seu filho *')
      .setRequired(true);

  // Configurações de confirmação
  form.setConfirmationMessage('Obrigado pela pré-inscrição! Entraremos em contato com mais detalhes sobre o Future Day. 🚀');

  Logger.log('Formulário criado: ' + form.getPublishedUrl());
  Logger.log('ID do formulário: ' + form.getId());
  
  return form.getPublishedUrl();
}

// Função para executar e abrir o formulário
function runAndOpenForm() {
  const url = createFutureDayForm();
  const html = HtmlService.createHtmlOutput(`<script>window.open('${url}'); google.script.host.close();</script>`)
      .setWidth(100)
      .setHeight(100);
  SpreadsheetApp.getUi().showModalDialog(html, 'Abrindo formulário...');
}