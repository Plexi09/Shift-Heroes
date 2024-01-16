import requests
import time

headers = {
    'Authorization': f'Bearer YOUR_API_TOKEN',
}

liste_initiale = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers). json()
nouvelle_liste = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers). json()

nb_request = 0
while liste_initiale == nouvelle_liste:
    nouvelle_liste = requests.get('https://shiftheroes.fr/api/v1/plannings?type=daily', headers=headers). json()
    nb_request = nb_request + 1
    print(f"{nb_request} | Pas de nouveau planning disponible...")
    time.sleep(1)

print("Nouveau planning disponible !")
new_planning_id = nouvelle_liste[0]["id"]
print(f"Nouveau ID: {new_planning_id}")


liste_creneaux = requests.get(f'https://shiftheroes.fr/api/v1/plannings/{new_planning_id}/shifts', headers=headers).json()

# Afficher les IDs des créneaux
for shift in liste_creneaux:
    shift_id = shift['id']
    print(f"L'id du créneau est : {shift_id}")

    # Réserver tous les créneaux de ce nouveau planning
    shift_taken = requests.post(f'https://shiftheroes.fr/api/v1/plannings/{new_planning_id}/shifts/{shift_id}/reservations', headers=headers)
print("Touts les créneaux ont été réservés !")
