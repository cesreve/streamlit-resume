import streamlit as st
import time
# --- FONCTIONS POUR STRUCTURER LE CV ---
def afficher_section(titre, contenu):
    st.subheader(titre)
    st.write(contenu)

# --- AFFICHAGE DES COMPÉTENCES TECHNIQUES ---
def afficher_liste_competences(competences):
    col1, col2 = st.columns(2)  # Divide skills into two columns
    for i, competence in enumerate(competences):
        if i % 2 == 0:  # Even index, display in the first column
            with col1:
                st.markdown(f"- {competence}")
        else:  # Odd index, display in the second column
            with col2:
                st.markdown(f"- {competence}")

# --- AFFICHAGE DE L'EXPÉRIENCE PROFESSIONNELLE ---
def afficher_experience(experience):
    titre_md = f"**{experience['poste']}** - {experience['entreprise']} ({experience['dates']})"  # Markdown H3 heading

    with st.expander(titre_md, expanded=False):
        st.write(experience['ville'])
        st.markdown(experience['description'])

# --- AFFICHAGE DES FORMATIONS ---
def afficher_formation(formation):
    titre_md = f"**{formation['intitule']}** - {formation['université']} ({formation['dates']})"  # Markdown H3 heading

    with st.expander(titre_md, expanded=False):
        st.write(formation['ville'])
        st.markdown(formation['description'])

# --- CONTENU DU CV ---
prenom_nom = "[Votre Prénom NOM]"
adresse = "[Votre Adresse]"
telephone = "[Votre Numéro de Téléphone]"
email = "[Votre Email]"
linkedin = "[Votre Profil LinkedIn (facultatif)]"

resume = """
Data Engineer expérimenté avec 5 ans d'expérience dans la conception, la construction et la maintenance de pipelines de données robustes et évolutifs. Expertise dans l'utilisation de technologies Big Data pour collecter, transformer et analyser de grands volumes de données. Passionné par l'optimisation des processus de données et la création de solutions pour améliorer la prise de décision basée sur les données.
"""

competences_techniques = [
    "Python", "SQL", "Apache Spark", "Hadoop", "Airflow",
    "PostgreSQL", "MySQL", "GCP (BigQuery, Dataflow)", "Power BI", "Docker", "Kubernetes"
]

# --- EXPÉRIENCE PROFESSIONNELLE ---
experience_pro = [
    {
        "entreprise": "Data Solutions Inc.",
        "ville": "Paris",
        "dates": "2022 - Présent",
        "poste": "Data Engineer Senior",
        "description": """
            - Leadership technique d'une équipe de 3 Data Engineers.
            - Conception et développement d'une plateforme de données en temps réel utilisant Apache Kafka et Spark Streaming pour le traitement de flux de données financières.
            - Mise en place d'un système de monitoring et d'alerting pour assurer la fiabilité et la performance des pipelines.
            - Réduction de 30% du temps de latence des traitements de données grâce à l'optimisation des requêtes Spark.
        """
    },
    {
        "entreprise": "Start-up Big Data",
        "ville": "Lyon",
        "dates": "2019 - 2022",
        "poste": "Data Engineer",
        "description": """
            - Construction d'un pipeline ETL complet pour l'intégration de données clients provenant de sources variées (CRM, ERP, fichiers CSV).
            - Utilisation d'Airflow pour l'orchestration des tâches et la gestion des dépendances.
            - Développement de modèles de données dimensionnels pour faciliter l'analyse et le reporting.
            - Amélioration de la qualité des données en implémentant des règles de validation et de nettoyage.
        """
    },
        {
        "entreprise": "Another Compagny",
        "ville": "Geneva",
        "dates": "2017 - 2019",
        "poste": "Data Engineer",
        "description": """
            - Construction d'un pipeline ETL complet pour l'intégration de données clients provenant de sources variées (CRM, ERP, fichiers CSV).
            - Utilisation d'Airflow pour l'orchestration des tâches et la gestion des dépendances.
            - Développement de modèles de données dimensionnels pour faciliter l'analyse et le reporting.
            - Amélioration de la qualité des données en implémentant des règles de validation et de nettoyage.
        """
    }
    # ... (Ajoutez d'autres expériences si nécessaire)
]
# --- FORMATION
formations = [
    {
        "université": "Université Lille",
        "ville": "Lille",
        "dates": "2022 - Présent",
        "intitule": "Master Data",
        "description": """
            - Suivre les cours (python, SQL, databases, machine learning)
            - Faire les TDs, mise en place d'une méthodologie agile de répartition des tâches entre les différents étudiants
            - Réviser pour les exams, approche cycle en V, analyse des spécifications, POC et mise en production
            - Réseauter pendant les soirées, pratique du rock en boîte de nuit
        """
    }
]
# --- LOISIRS --- 
langues = ["🇫🇷 Français (courant)", "🇬🇧 Anglais (professionnel)"]  # Emojis drapeau
loisirs = ["🥾 Randonnée", "📚 Lecture", "🎸 Guitare", "✈️ Voyage"]     # Emojis loisirs

#----------------------------
# --- INTERFACE STREAMLIT ---
st.set_page_config(page_title="CV Data Engineer", page_icon=":computer:", layout="wide")
#
# --- INFORMATIONS PERSONNELLES ---
st.title(prenom_nom)
col1, col2 = st.columns([1, 1])  # Ajustez les proportions si nécessaire
    
with col2:
    st.write(f"**📱 Téléphone:** {telephone}")
    st.write(f"**📧 Email:** {email}")
    st.write(f"**📍 Adresse:** {adresse}")
    if linkedin:
        st.write(f"**🔗 LinkedIn:** [{linkedin}]({linkedin})")

# --- COMPÉTENCES TECHNIQUES ET EXPÉRIENCE PROFESSIONNELLE ---
col1, col2 = st.columns([3, 7])  # Ajustez les proportions si nécessaire

with col1:
    with st.container(border=True):
        with st.container(border=True):
            afficher_section("🛠️ COMPÉTENCES TECHNIQUES", "")
            afficher_liste_competences(competences_techniques)

        with st.container(border=True):
            afficher_section("🗣️ LANGUES", "")
            for langue in langues:
                st.markdown(f"- {langue}")

        with st.container(border=True):
            afficher_section("🏖️ LOISIRS", "")
            for loisir in loisirs:
                st.markdown(f"- {loisir}")  # Affichage des loisirs

with col2:
    with st.container(border=True):
        afficher_section("📋 RÉSUMÉ", "")  # On supprime resume ici
        st.markdown(
            f'<p class="resume-text">{resume}</p>', unsafe_allow_html=True
        )  # Appliquer la classe CSS au texte

    with st.container(border=True):
        afficher_section("💼 EXPÉRIENCE PROFESSIONNELLE", "")
        for exp in experience_pro:
            afficher_experience(exp)

    with st.container(border=True):
        afficher_section("💼 FORMATIONS", "")
        st.write("**📱 UNi:** ")
        for form in formations:
            afficher_formation(form)
            
# --- CUSTOM CSS FOR CONTAINERS ---
st.markdown("""
<style>
.stApp {
    max-width: 1200px; /* Adjust the width value as needed */
    margin: 0 auto;  /* Center the content horizontally */
}
.stContainer {
    border: 1px solid lightgray;
    padding: 10px;
    border-radius: 5px;
    margin-bottom: 20px; 
    width: 90%; /* Take up 90% of the available width */
    max-width: 800px; /* Adjust the maximum width as needed */
}
/* ... autres styles ... */
.resume-text { /* Nouveau style pour le texte du résumé */
    text-align: justify;
}
</style>

""", unsafe_allow_html=True)
