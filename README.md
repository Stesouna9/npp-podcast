# NPP — Ne paniquez pas ! On va tout faire péter

Site de l'émission podcast de Doc Laundal et Tesla_burger.

## Fichiers

- `index.html` — toute la page
- `style.css` — l'habillage
- `apps.css` — habillage des pages apps
- `apps/`, `kotoba/`, `voteday/`, `support/`, `confidentialite/` — site des apps OKALAM Studio
- `marketing/` — journal des idées de promo (routine nocturne)

## À compléter

1. **Lien Discord** : dans `index.html`, bouton « Rejoindre le serveur » (`id="discord-link"`),
   remplacer `href="#"` par le lien d'invitation permanent du serveur.
2. **Adresse mail** : section Contact, remplacer `contact@example.com`.
3. **Épisodes** : dupliquer le bloc `<li class="episode">` pour chaque nouvel épisode,
   retirer la classe `soon` et ajouter le lien d'écoute.

## Publication

Le site est publié par GitHub Pages depuis la branche `main`.
Chaque `git push` met le site à jour en une minute environ.
