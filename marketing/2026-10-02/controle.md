# Contrôle des liens — npp-podcast (branche marketing/2026-10-02, 2026-10-02)

## Limite importante
Tous les tests HTTP externes ont échoué avec `CONNECT tunnel failed, response 403` : le proxy d'egress de l'environnement refuse ces domaines (politique d'organisation). Ce n'est pas une réponse des sites. D'après /root/.ccr/README.md, les refus 403/407 ne se réessaient pas et la vérification TLS n'a pas été désactivée. Aucun lien externe n'est donc confirmé ni infirmé ici : à retester depuis un poste avec accès réseau libre. Aucun fichier du dépôt n'a été modifié.

## Liens externes
| Lien | Statut HTTP | Verdict | Fichier source |
|---|---|---|---|
| https://apps.apple.com/fr/app/voteday/id6760981728 | aucun (403 proxy) | NON VÉRIFIABLE (proxy) ; à retester, doit renvoyer 200 | voteday/index.html |
| https://podcasts.apple.com/fr/podcast/id6804104531 | aucun (403 proxy) | NON VÉRIFIABLE (proxy) ; à retester | index.html |
| https://www.youtube.com/@NPPOVTFP | aucun (403 proxy) | NON VÉRIFIABLE (proxy) ; à retester | index.html |
| https://podcast.ausha.co/nppovtfp | aucun (403 proxy) | NON VÉRIFIABLE (proxy) ; à retester | index.html |
| https://discord.gg/a42kMBcp4a | aucun (403 proxy) | NON VÉRIFIABLE (bloque les bots) | index.html, apps/, kotoba/, voteday/, support/, confidentialite/ |
| https://apps.apple.com/…/id6761341663 (Kotoba) | aucun (403 proxy) | ATTENDU (404 normal avant validation Apple) ; non testé. Ce lien n'existe pas dans le dépôt : kotoba/index.html n'a pas de bouton App Store | kotoba/index.html (absent) |
| mailto:nppovtfp@gmail.com | n/a | OK (syntaxe valide) | index.html |
| mailto:contact@okalamstudio.com (avec et sans ?subject=Support%20OKALAM%20Studio) | n/a | OK (syntaxe valide) | support/, confidentialite/ |

## Liens de partage (structure vérifiée statiquement)
| Lien | Verdict | Fichier source |
|---|---|---|
| https://wa.me/?text=D%C3%A9couvre%20Kotoba%20et%20VoteDay | OK (structure, texte encodé) ; NON VÉRIFIABLE en HTTP | apps/index.html |
| https://twitter.com/intent/tweet?text=D%C3%A9couvre%20Kotoba%20et%20VoteDay | OK (structure, texte encodé) ; NON VÉRIFIABLE en HTTP | apps/index.html |
| https://www.reddit.com/submit?title=D%C3%A9couvre%20Kotoba%20et%20VoteDay | Structure OK ; Reddit exige en pratique `url=` ou `text=` : sans URL, le formulaire s'ouvre vide de lien. NON VÉRIFIABLE (bloque les bots) | apps/index.html |
| wa.me / twitter / reddit avec « Kotoba — le jeu de mots en 6 essais » (%E2%80%94 correct) | idem ci-dessus | kotoba/index.html |
| wa.me / twitter / reddit avec « VoteDay — une question par jour, vote A ou B » (%2C, %20 corrects) | idem ci-dessus | voteday/index.html |

Remarque : aucun lien de partage n'inclut l'URL de la page (`&url=` pour X, URL dans `text=` pour WhatsApp). Le partage n'envoie donc que du texte. Les boutons « Partager » (id share-btn) passent par navigator.share ou le presse-papiers.

## Liens internes (cibles vérifiées dans le dépôt)
| Lien | Verdict | Fichier source |
|---|---|---|
| style.css?v=4, apps.css?v=1 (+ variantes ../) | OK : fichiers présents | toutes les pages |
| img/favicon.png, img/logo.png | OK | index.html et sous-pages |
| img/banniere.png (og:image) | OK : présent | index.html |
| img/apps/kotoba-icon.png, voteday-icon.png | OK | apps/, kotoba/, voteday/ |
| img/apps/kotoba-feature.jpg, kotoba-01_home, 02_game, 03_adventure, 04_store | OK : présents | kotoba/index.html |
| img/apps/voteday-feature.jpg, 01_menu, 02_vote, 03_bubl_du_jour, 04_ile, 06_cartes | OK : présents | voteday/index.html |
| Pages ../apps/, ../kotoba/, ../voteday/, ../support/, ../confidentialite/, ../, kotoba/, voteday/, apps/, support/ | OK : index.html présent | toutes les pages |
| Ancres #ecouter, #soutenir | OK : ids présents dans index.html | index.html |
| README.md `href="#"` | Ancre vide, sans cible (anodin) | README.md |
| marketing/ideas-log.md, apps.css, style.css | Aucun lien ni url() détecté | n/a |

## Autres contrôles
- Images sans alt : aucune (toutes les balises img ont un alt non vide). OK.
- target="_blank" sans rel=noopener : aucun (tous les liens ont rel="noopener"). OK.
- og:image : présente sur les 6 pages. Attention : toutes les valeurs sont des chemins relatifs (`img/banniere.png`, `../img/apps/…`). Les crawlers (Facebook, X, WhatsApp, Discord) exigent une URL absolue : l'aperçu ne s'affichera probablement pas. À corriger avec l'URL publique du site. Pas de twitter:card ni de og:url non plus.
- support/, apps/ et confidentialite/ réutilisent kotoba-feature.jpg comme og:image (choix éditorial, pas une erreur).
