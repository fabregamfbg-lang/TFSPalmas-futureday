import streamlit as st
import qrcode
from io import BytesIO
import pandas as pd
from datetime import datetime
import os

st.set_page_config(
    page_title="Pré-Inscrição Future Day",
    page_icon="🚀",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# CSS customizado
st.markdown("""
<style>
    .main { padding-top: 1rem; }
    .stButton>button { 
        background: linear-gradient(90deg, #6366f1 0%, #8b5cf6 100%);
        color: white; border: none; border-radius: 8px; 
        padding: 0.75rem 2rem; font-size: 1.1rem; font-weight: 600;
        width: 100%; margin-top: 1rem;
    }
    .stButton>button:hover { 
        background: linear-gradient(90deg, #4f46e5 0%, #7c3aed 100%);
        transform: translateY(-1px); box-shadow: 0 4px 12px rgba(99,102,241,0.4);
    }
    .header-text { text-align: center; margin-bottom: 2rem; }
    .highlight { background: linear-gradient(90deg, #6366f1, #8b5cf6); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
    .qr-container { text-align: center; margin: 1.5rem 0; }
    .footer { text-align: center; color: #6b7280; font-size: 0.85rem; margin-top: 2rem; }
    [data-testid="stForm"] { border: none; box-shadow: none; padding: 0; }
</style>
""", unsafe_allow_html=True)

# ---------- CONFIG ----------
FORM_CSV = "respostas_future_day.csv"
LOCATION_URL = "https://goo.su/iQNN7P"  # SUBSTITUA PELO SEU LINK
LOGO_PATH = "logo.png"  # COLOQUE SUA LOGO NA MESMA PASTA

# ---------- FUNÇÕES ----------
def init_csv():
    if not os.path.exists(FORM_CSV):
        df = pd.DataFrame(columns=[
            "timestamp", "nome_responsavel", "nascimento_responsavel", 
            "endereco", "telefone", "nome_filho", "nascimento_filho"
        ])
        df.to_csv(FORM_CSV, index=False)

def save_response(data):
    df = pd.read_csv(FORM_CSV)
    new_row = pd.DataFrame([data])
    df = pd.concat([df, new_row], ignore_index=True)
    df.to_csv(FORM_CSV, index=False)

def generate_qr_code(url):
    qr = qrcode.QRCode(version=1, box_size=10, border=4)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="#6366f1", back_color="white")
    buf = BytesIO()
    img.save(buf, format="PNG")
    return buf.getvalue()

def validate_form(nome_resp, nascimento_resp, endereco, telefone, nome_filho, nascimento_filho):
    errors = []
    if not nome_resp.strip(): errors.append("Nome do responsável é obrigatório")
    if not nascimento_resp: errors.append("Data de nascimento do responsável é obrigatória")
    if not endereco.strip(): errors.append("Endereço é obrigatório")
    if not telefone.strip(): errors.append("Telefone/WhatsApp é obrigatório")
    if not nome_filho.strip(): errors.append("Nome do filho é obrigatório")
    if not nascimento_filho: errors.append("Data de nascimento do filho é obrigatória")
    return errors

# ---------- INICIALIZAÇÃO ----------
init_csv()

# ---------- HEADER ----------
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    if os.path.exists("logo.jpg"):
        st.image(logo.jpg, width=180)
    else:
        st.markdown("### 🚀 Future Day")
cd "C:\Users\fabio\Documents\Default Project"
git add app.py
git commit -m "Fix logo path and location URL"
git push origin main

st.markdown("""
<div class="header-text">
    <h1>Pré-Inscrição <span class="highlight">Future Day</span></h1>
    <p style="color: #6b7280; font-size: 1.1rem;">Falta pouco para o grande dia! 🥳</p>
</div>
""", unsafe_allow_html=True)

# ---------- DESCRIÇÃO ----------
with st.expander("📋 **Sobre o evento**", expanded=True):
    st.markdown("""
A inauguração da **The Future School** está chegando, e você e seu filho estão oficialmente convidados.

Esse não vai ser um evento qualquer. Vai ser a chance do seu filho colocar a mão na massa de verdade e viver um pouquinho do que é aprender por aqui.

**No dia, os alunos irão:**
- 🤖 Aprender a criar mecanismos automatizados no **Minecraft**
- 👾 Dar os primeiros passos na programação dentro do **Roblox**
- 🏆 Concorrer a prêmios especiais durante o evento!

**E tem mais:** quem estiver presente garante acesso aos nossos **descontos de fundador**, uma condição exclusiva para as primeiras famílias que entrarem nessa história com a gente.

**📍 Endereço:** Pista do Antigo Aeroporto, próximo a Havan

> **⚠️ IMPORTANTE:** AS INSCRIÇÕES OFICIAIS SERÃO REALIZADAS **2 DIAS ANTES DO EVENTO**
""")

# ---------- QR CODE LOCALIZAÇÃO ----------
st.markdown('<div class="qr-container">', unsafe_allow_html=True)
st.markdown("### 📍 Localização do Evento")
qr_img = generate_qr_code("https://goo.su/iQNN7P")
st.image(qr_img, width=200, caption="Escaneie para abrir no Google Maps")
st.caption(f"[Abrir no Google Maps]({https://goo.su/iQNN7P})")
st.markdown('</div>', unsafe_allow_html=True)

# ---------- FORMULÁRIO ----------
st.markdown("---")
st.markdown("### 📝 Formulário de Pré-Inscrição")
st.caption("Campos marcados com * são obrigatórios")

with st.form("future_day_form", clear_on_submit=False):
    col1, col2 = st.columns(2)
    
    with col1:
        nome_responsavel = st.text_input("**Qual o seu nome completo? ***", placeholder="João da Silva")
        nascimento_responsavel = st.date_input(
            "**Qual sua data de nascimento? ***", 
            min_value=datetime(1940, 1, 1), 
            max_value=datetime.now(),
            format="DD/MM/YYYY"
        )
        endereco = st.text_area("**Qual seu endereço? ***", placeholder="Rua, número, bairro, cidade", height=100)
    
    with col2:
        telefone = st.text_input("**Qual seu telefone/WhatsApp? ***", placeholder="(47) 9 9999-9999")
        nome_filho = st.text_input("**Qual o nome do seu filho? ***", placeholder="Maria da Silva")
        nascimento_filho = st.date_input(
            "**Qual a data de nascimento do seu filho? ***",
            min_value=datetime(2005, 1, 1),
            max_value=datetime.now(),
            format="DD/MM/YYYY"
        )
    
    submitted = st.form_submit_button("✅ Confirmar Pré-Inscrição", use_container_width=True)

    if submitted:
        errors = validate_form(nome_responsavel, nascimento_responsavel, endereco, telefone, nome_filho, nascimento_filho)
        
        if errors:
            for error in errors:
                st.error(error)
        else:
            data = {
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                "nome_responsavel": nome_responsavel.strip(),
                "nascimento_responsavel": nascimento_responsavel.strftime("%Y-%m-%d"),
                "endereco": endereco.strip(),
                "telefone": telefone.strip(),
                "nome_filho": nome_filho.strip(),
                "nascimento_filho": nascimento_filho.strftime("%Y-%m-%d")
            }
            save_response(data)
            
            st.success("🎉 **Pré-inscrição realizada com sucesso!**")
            st.balloons()
            st.markdown("""
            > **Próximos passos:** Entraremos em contato via WhatsApp com mais detalhes sobre o Future Day e as inscrições oficiais (que abrem 2 dias antes do evento).
            
            Fique de olho no celular! 📱
            """)

# ---------- ADMIN (opcional - só aparece com senha) ----------
with st.expander("🔐 Área Admin (visualizar respostas)"):
    admin_pass = st.text_input("Senha admin", type="password", placeholder="Digite a senha para ver respostas")
    if admin_pass == "futureday2024":  # ALTERE ESSA SENHA!
        df = pd.read_csv(FORM_CSV)
        st.metric("Total de inscrições", len(df))
        st.dataframe(df, use_container_width=True, hide_index=True)
        
        csv = df.to_csv(index=False).encode('utf-8')
        st.download_button(
            "📥 Baixar CSV", 
            csv, 
            f"inscricoes_future_day_{datetime.now().strftime('%Y%m%d')}.csv",
            "text/csv",
            use_container_width=True
        )
    elif admin_pass:
        st.error("Senha incorreta")

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
    <hr style="margin: 1.5rem 0; border-color: #e5e7eb;">
    <p>The Future School • Pré-Inscrição Future Day</p>
    <p>Desenvolvido com 💜 usando Streamlit</p>
</div>
""", unsafe_allow_html=True)
