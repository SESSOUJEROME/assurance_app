import streamlit as st

# Titre de l'application
st.set_page_config(page_title="Tarification Assurance Dommage", page_icon=":shield:")

# Introduction générale
st.title("Bienvenue sur notre Plateforme de Tarification d'Assurance Dommage")
st.write(
    "Utilisez notre outil pour calculer les primes d'assurance de manière précise "
    "et personnalisée. Sélectionnez une option dans le menu pour commencer."
)


# Affichage du contenu de la page d'accueil
st.write("Cette application est conçue pour aider les assureurs à calculer les primes en fonction des risques individuels des assurés.")


# Redirection vers la page de calcul de prime
if st.button("Commencez maintenant"):
    st.switch_page("pages/2_🧮Calculateur.py")

