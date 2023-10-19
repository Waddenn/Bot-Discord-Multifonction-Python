# Bot Discord Multifonction

## Description:
Ce bot Discord a été conçu par Lbutynski et Wade dans le cadre d'un projet scolaire d'une journée. Il est conçu pour offrir une variété de petites fonctionnalités utiles pour les membres d'un serveur Discord.

## 🚀 Fonctionnalités principales (obligatoires) :

### 1. Salutations:
   - Le bot envoie un message de bienvenue dans un canal spécifique lorsque qu'un nouvel utilisateur rejoint le serveur.

### 2. Informations sur le serveur:
   - Les utilisateurs peuvent demander des informations sur le serveur comme le nombre total de membres, le nombre de membres en ligne, le nombre de canaux, etc.

### 3. Gestion des sondages:
   - Les utilisateurs peuvent créer des sondages simples où d'autres membres peuvent voter en utilisant des réactions.

### 4. Convertisseur de devises:
   - Les utilisateurs peuvent convertir un montant d'une devise à une autre.

## 📌 Fonctionnalités supplémentaires (facultatives) :

### 5. Modérateur:
   - Le bot détecte et supprime automatiquement des messages contenant des mots interdits.
   - Les modérateurs du serveur peuvent demander au bot de bannir ou de mettre en sourdine un utilisateur spécifique.

### 6. Chifoumi:
   - Les utilisateurs peuvent jouer à un jeu de pierre-papier-ciseaux contre le bot.

## 📜 Commandes:

- **Modération**:
  - `!kick @[User] [raison]` - Expulse un utilisateur pour une raison donnée.
  - `!ban @[User] [raison]` - Bannit un utilisateur pour une raison donnée.
  - `!mute @[User] duration [raison]` - Met un utilisateur en sourdine pour une durée déterminée.

- **Sondages**:
  - `!poll options [question] [Option 1] [Option 2] ... [Option N]` - Crée un sondage avec plusieurs options.
  - `!poll simple [question]` - Crée un sondage simple.

- **Informations sur le serveur**:
  - `!membersCount` - Affiche le nombre total de membres sur le serveur.
  - `!channelCount` - Affiche le nombre total de canaux sur le serveur.

- **Convertisseur de devises**:
  - `!convert [montant] [devises de départ] [devises d'arrivée]` - Convertit un montant d'une devise à une autre.

- **Chifoumi**:
  - `!chifoumi [pierre, feuille, ciseaux]` - Joue à pierre-papier-ciseaux contre le bot.

