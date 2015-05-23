# Spécifications

Document relatant des besoins du projet afin de déterminer la cible à atteindre.

## Constat

La recherche d'un emploi est fastidieuse aussi bien dans la recherche elle-même qui s'effectue de manière physique que papier/numérique. Physique car il faut se déplacer, chercher sur place, prendre des rendez-vous, effectuer des entretiens, etc.<br />
Papier/numérique car il faut **suivre** sa recherche d'emploi que ce soit en listant les entreprises à contacter, en mettant à jour sa liste, en notant les actions entreprises sur une société particulière, etc.

## But recherché

Pour faciliter cette recherche d'emploi, il serait intéressant de pouvoir en améliorer le suivi.

## Fonctionnement de la recherche d'un emploi

Je vais décrire en plusieurs phrases les éléments relatifs au suivi des candidatures pour la recherche d'un emploi.

Ces éléments devraient permettre d'exprimer le besoin réel et trouver une manière de modéliser notre projet.

Je vous renvoie à [mon analyse de la recherche d'un emploi](analyse.html) afin de comprendre mon étude du problème.

## Recherche d'une solution

Après mon analyse, il est temps de décrire une solution à ce suivi de recherche d'un emploi.

Il faut bien garder en tête les éléments suivants : 

  * recherche d'informations sur l'entreprise
  * recherche de contacts
  * appels/relances fréquents sur les entreprises
  * traitement des réponses

Il faut donc veiller à ce que ces éléments se retrouvent rapidement à la disposition de l'utilisateur, par exemple en page d'accueil sous la forme d'un dashboard récapitulatif des actions à effectuer dans la journée.

Je dégage donc plusieurs "objets" de tout cela : 

  * entreprise : qui contient l'ensemble des entreprises/organismes et leurs informations
  * contact : une personne attachée à une entreprise ou un organisme
  * canal : le mode d'envoi du message parmi ceux cités dans l'analyse (courriel, courrier postal, appel téléponique, etc.)
  * message : ce qu'on envoie à une entreprise. Peut contenir des documents attachés : CV, Lettre de motivation, etc. Un message utilise un canal spécifique. Peut aussi être une réponse
  * document : un document (CV, lettre de motivation) utilisable dans plusieurs messages
  * action : se définit par un message à envoyer à un contact (ou aucun) d'une entreprise à une date prévue. Peut être effectué à une autre date (date_effectuée).

D'autres objets viendront se greffer à ceux là en cours de développement, suivant les nouvelles idées.

Je détaille plus avant la solution dans [ma conception de ce logiciel de suivi de recherche d'emploi](concept.html).
