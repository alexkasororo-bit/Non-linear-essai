import streamlit as st
import math

# Titre et description de l'application
st.title("Application Dufay - Résolution d'équations non linéaires")
st.write("""
    Cette application vous permet de résoudre toutes les équations non linéaires avec x comme variable. 
    Vous fournirez une fonction \(f(x)\), ainsi que deux bornes de l'intervalle, et l'application appliquera la méthode de la sécante pour trouver la racine approximée.
""")

# Entrée de la fonction f(x) par l'utilisateur
f_str = st.text_input("Entrez votre fonction non linéaire f(x) (en termes de x):", "x**2 - 9")

# Entrée des bornes de l'intervalle
x0 = st.number_input("Entrez la première borne de l'intervalle (x0):", value=0.0)
x1 = st.number_input("Entrez la seconde borne de l'intervalle (x1):", value=2.0)

# Paramètres de la méthode de la sécante
tol = 1e-100  # Tolérance pour l'erreur de la solution
max_it = 1000  # Nombre maximum d'itérations

# Méthode de la sécante
if st.button("Résoudre l'équation"):
    it = 0
    r1 = eval(f_str, {"__builtins__": {}}, {"x": x0, "math": math})
    r2 = eval(f_str, {"__builtins__": {}}, {"x": x1, "math": math})
    
    
    while it < max_it:
        fx0 = r1
        fx1 = r2
        # Vérifier si une des valeurs est déjà une racine
        if abs(fx0) < tol:
            st.success(f"La racine trouvée est : x = {x0} après {it} itérations.")
            st.write(f"La valeur de f(x) est : {fx0}")
            break
        if abs(fx1) < tol:
            st.success(f"La racine trouvée est : x = {x1} après {it} itérations.")
            st.write(f"La valeur de f(x) est : {fx1}")
            break
        
        # Calcul de la nouvelle approximation x2
        if fx1 - fx0 == 0:
            st.error("La division par zéro n'est pas possible! Les bornes choisies ne sont pas adaptées.")
            break
        
        x2 = x1 - fx1 * (x1 - x0) / (fx1 - fx0)
        
        # Actualisation des valeurs
        x0 = x1
        x1 = x2
        r1 = eval(f_str, {"__builtins__": {}}, {"x": x0, "math": math})
        r2 = eval(f_str, {"__builtins__": {}}, {"x": x1, "math": math})
        it += 1
        
        # Vérifier la convergence
        if abs(x1 - x0) < tol:
            st.success(f"La racine approximée est : x ≈ {x1} après {it} itérations.")
            st.write(f"La valeur de f(x) est : {r2}")
            break
    else:
        st.warning("Méthode non convergée dans le nombre maximum d'itérations. Veuillez choisir de nouvelles bornes au départ.")
