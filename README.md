# ttsbot

ttsbot is a [Telepot](https://telepot.readthedocs.io/en/latest/) powerd, easy to use Telegram bot allowing you to convert text to speech
using [Reverso Translations](https://www.reverso.net).

#### Credits:
=======

- [Reverso Translations](https://www.reverso.net).
- [Yuval Mejahez](https://github.com/rt400) for creating [pyttsreverso](https://github.com/rt400/pyttsreverso)


### ttsbot supports the following languages:
===========================================

The language to use. Supported languages are in this table , please use only the name from **LangCode** column:

| LangCode | Voice | Gender | Language |
| ------------- | ------------- | ------------- | ------------- |
| Leila-Arabic | Leila22k | Female | Arabic |
| Mehdi-Arabic | Mehdi22k | Male | Arabic |
| Nizar-Arabic | Nizar22k | Male | Arabic |
| Salma-Arabic | Salma22k | Female | Arabic |
| Lisa-Australian-English | Lisa22k | Female | Australian English |
| Tyler-Australian-English | Tyler22k | Male | Australian English |
| Jeroen-Belgian-Dutch | Jeroen22k | Male | Belgian Dutch |
| Sofie-Belgian-Dutch | Sofie22k | Female | Belgian Dutch |
| Zoe-Belgian-Dutch | Zoe22k | Female | Belgian Dutch |
| Alice-BE-Belgian-French | Alice-BE22k | Female | Belgian French |
| Anais-BE-Belgian-French | Anais-BE22k | Female | Belgian French |
| Antoine-BE-Belgian-French | Antoine-BE22k | Male | Belgian French |
| Bruno-BE-Belgian-French | Bruno-BE22k | Male | Belgian French |
| Claire-BE-Belgian-French | Claire-BE22k | Female | Belgian French |
| Julie-BE-Belgian-French | Julie-BE22k | Female | Belgian French |
| Justine-Belgian-French | Justine22k | Female | Belgian French |
| Manon-BE-Belgian-French | Manon-BE22k | Female | Belgian French |
| Margaux-BE-Belgian-French | Margaux-BE22k | Female | Belgian French |
| Marcia-Brazilian | Marcia22k | Female | Brazilian |
| Graham-British | Graham22k | Male | British |
| Lucy-British | Lucy22k | Female | British |
| Peter-British | Peter22k | Male | British |
| QueenElizabeth-British | QueenElizabeth22k | Female | British |
| Rachel-British | Rachel22k | Female | British |
| Louise-Canadian-French | Louise22k | Female | Canadian French |
| Laia-Catalan | Laia22k | Female | Catalan |
| Eliska-Czech | Eliska22k | Female | Czech |
| Mette-Danish | Mette22k | Female | Danish |
| Rasmus-Danish | Rasmus22k | Male | Danish |
| Daan-Dutch | Daan22k | Male | Dutch |
| Femke-Dutch | Femke22k | Female | Dutch |
| Jasmijn-Dutch | Jasmijn22k | Female | Dutch |
| Max-Dutch | Max22k | Male | Dutch |
| Samuel-Finland-Swedish | Samuel22k | Male | Finland Swedish |
| Sanna-Finnish | Sanna22k | Female | Finnish |
| Alice-French | Alice22k | Female | French |
| Anais-French | Anais22k | Female | French |
| Antoine-French | Antoine22k | Male | French |
| Bruno-French | Bruno22k | Male | French |
| Claire-French | Claire22k | Female | French |
| Julie-French | Julie22k | Female | French |
| Manon-French | Manon22k | Female | French |
| Margaux-French | Margaux22k | Female | French |
| Andreas-German | Andreas22k | Male | German |
| Claudia-German | Claudia22k | Female | German |
| Julia-German | Julia22k | Female | German |
| Klaus-German | Klaus22k | Male | German |
| Sarah-German | Sarah22k | Female | German |
| Kal-Gothenburg-Swedish | Kal22k | Male | Gothenburg Swedish |
| Dimitris-Greek | Dimitris22k | Male | Greek |
| he-IL-Asaf-Hebrew | he-IL-Asaf | Male | Hebrew |
| Deepa-Indian-English | Deepa22k | Female | Indian English |
| Chiara-Italian | Chiara22k | Female | Italian |
| Fabiana-Italian | Fabiana22k | Female | Italian |
| Vittorio-Italian | Vittorio22k | Male | Italian |
| Sakura-Japanese | Sakura22k | Female | Japanese |
| Minji-Korean | Minji22k | Female | Korean |
| Lulu-Mandarin-Chinese | Lulu22k | Female | Mandarin Chinese |
| Bente-Norwegian | Bente22k | Female | Norwegian |
| Kari-Norwegian | Kari22k | Female | Norwegian |
| Olav-Norwegian | Olav22k | Male | Norwegian |
| Ania-Polish | Ania22k | Female | Polish |
| Monika-Polish | Monika22k | Female | Polish |
| Celia-Portuguese | Celia22k | Female | Portuguese |
| ro-RO-Andrei-Romanian | ro-RO-Andrei | Male | Romanian |
| Alyona-Russian | Alyona22k | Female | Russian |
| Mia-Scanian | Mia22k | Female | Scanian |
| Antonio-Spanish | Antonio22k | Male | Spanish |
| Ines-Spanish | Ines22k | Female | Spanish |
| Maria-Spanish | Maria22k | Female | Spanish |
| Elin-Swedish | Elin22k | Female | Swedish |
| Emil-Swedish | Emil22k | Male | Swedish |
| Emma-Swedish | Emma22k | Female | Swedish |
| Erik-Swedish | Erik22k | Male | Swedish |
| Ipek-Turkish | Ipek22k | Female | Turkish |
| Heather-US-English | Heather22k | Female | US English |
| Karen-US-English | Karen22k | Female | US English |
| Kenny-US-English | Kenny22k | Male | US English |
| Laura-US-English | Laura22k | Female | US English |
| Micah-US-English | Micah22k | Male | US English |
| Nelly-US-English | Nelly22k | Female | US English |
| Rod-US-English | Rod22k | Male | US English |
| Ryan-US-English | Ryan22k | Male | US English |
| Saul-US-English | Saul22k | Male | US English |
| Sharon-US-English | Sharon22k | Female | US English |
| Tracy-US-English | Tracy22k | Female | US English |
| Will-US-English | Will22k | Male | US English |
| Rodrigo-US-Spanish | Rodrigo22k | Male | US Spanish |
| Rosa-US-Spanish | Rosa22k | Female | US Spanish |

### The Default language is "Sharon-US-English"

## Usage
### Run from hub

#### docker-compose from hub
```yaml
version: "3.7"

services:
 ttsbot:
    image: techblog/ttsbot
    container_name: ttsbot
    restart: always
    labels:
      - "com.ouroboros.enable=true"
    environment:
      - BOT_API_KEY=
      - TTS_LANG=he-IL-Asaf-Hebrew
      - TTS_PITCH=100
      - TTS_BITRATE=128k
```
Replace API_KEY with your bot token. if you do not have existing bot you can create one
using the instruction in Step 2 in this article:
[TelePi – Control your pi with Telegram Bot](https://en.techblog.co.il/2018/08/11/telepi-control-your-pi-with-telegram-bot/) 


# Donation
<br>
If you find this project helpful, you can give me a cup of coffee :) 

[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=8CGLEHN2NDXDE)
