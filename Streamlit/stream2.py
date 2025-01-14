import streamlit as st

# Titre de l'application
st.title('London Fire Brigade')

# Ajouter du CSS personnalisé pour les titres et le texte
st.markdown(
    """
    <style>
    .titre-principal {
        color: #FF0000;  /* Couleur rouge */
        font-size: 48px;
        text-align: center;
    }
    .texte {
        color: #f39c12;
        font-size: 24px;
    }
    .image-locale {
        position: absolute;
        top: 0;
        right: 0;
        width: 100px; 
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Utiliser des classes CSS dans HTML
st.markdown('<h1 class="titre-principal">Bonjour, Bienvenue sur notre projet !</h1>', unsafe_allow_html=True)
st.markdown("<p class='texte'>Les Temps d'intervention de la Brigade des Pompiers de Londres.</p>", unsafe_allow_html=True)

# Ajouter une image locale avec des styles CSS

st.image(r"C:\Users\Meylouu\Brigade Pompier\LBP1.jpg", use_container_width=True)

# Mettre des Onglets

tab1, tab2, tab3 = st.tabs(["Onglet 1", "Onglet 2", "Onglet 3"]) 
with tab1: 
    st.header("Contenu de l'Onglet 1") 
    st.write("Voici le contenu du premier onglet.") 

with tab2: 
    st.header("Contenu de l'Onglet 2") 
    st.write("Voici le contenu du deuxième onglet.") 
    
with tab3: 
    st.header("Contenu de l'Onglet 3") 
    st.write("Voici le contenu du troisième onglet.")