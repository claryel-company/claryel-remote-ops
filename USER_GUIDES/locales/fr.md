# CLARYEL RemoteOps — installation et configuration privée

RemoteOps gère votre propre ordinateur Windows, Ubuntu/Linux ou macOS via le chat IA que vous choisissez.

## 1. Installer

- [Installateur Windows](../../installers/install-windows.ps1)
- [Installateur macOS](../../installers/install-macos.sh)
- [Installateur Ubuntu](../../installers/install-ubuntu.sh)

Exécutez le fichier téléchargé. RemoteOps s’installe dans votre profil utilisateur, crée un espace local privé et ne désactive aucune protection du système.

## 2. Créer votre dépôt personnel Private

Installez GitHub CLI, exécutez `gh auth login`, puis la commande affichée par l’installateur :

```text
remoteops connect --path VOTRE-CHEMIN-PRIVE --create-private remoteops-mon-ordinateur
```

Le dépôt est créé dans votre compte GitHub avec la visibilité `Private`. RemoteOps ne le rend pas public et n’ajoute aucun collaborateur.

Private signifie caché du public. Vous, les personnes ou applications que vous autorisez et GitHub comme opérateur du service pouvez toujours y accéder. Protégez le compte avec une passkey ou l’authentification à deux facteurs.

Ne stockez jamais dans Git mots de passe, jetons, clés, codes de récupération, fichiers personnels, conversations, journaux bruts, bases de données ou sauvegardes.

## 3. Vérifier la confidentialité

```text
remoteops privacy-check --path VOTRE-CHEMIN-PRIVE
```

Continuez uniquement si le résultat affiche `"ok": true`, `"visibility": "PRIVATE"` et aucun signalement.

## 4. Connecter ChatGPT

1. Ouvrez **ChatGPT > Paramètres > Apps > GitHub**.
2. Choisissez **Uniquement les dépôts sélectionnés**.
3. Sélectionnez seulement `remoteops-mon-ordinateur`.
4. Vérifiez les autorisations avant d’accepter.
5. Vérifiez **Paramètres > Contrôles des données > Améliorer le modèle pour tous**.
6. Ne collez jamais de secrets ou fichiers personnels dans le chat.

La disponibilité de l’app GitHub et l’écriture dépendent du forfait et du mode ChatGPT. Une connexion en lecture seule ne peut pas appliquer de modifications.

## Limite des communications

RemoteOps contacte GitHub uniquement lors de la connexion ou synchronisation de votre dépôt privé, ChatGPT uniquement quand vous l’utilisez, et les sources de paquets uniquement pour les opérations logicielles approuvées. Les installateurs n’ajoutent ni publicité ni analyse étrangère.

Guides détaillés : [dépôt privé](../../docs/PRIVATE_REPOSITORY_SETUP.md), [ChatGPT](../../docs/CHATGPT_SETUP.md), [confidentialité et réseau](../../docs/PRIVACY_AND_NETWORK.md).
