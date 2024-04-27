from discord.ext import commands
import discord
from main import bot
import random

slap_gifs = ["https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGh4MzFwOTh6a3kybDRoODJ3Y3h5MG9qdXZuaTF3YnBkY3E4cHN4NCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/gSIz6gGLhguOY/giphy.gif",
             "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbGh4MzFwOTh6a3kybDRoODJ3Y3h5MG9qdXZuaTF3YnBkY3E4cHN4NCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/uG3lKkAuh53wc/giphy.gif",
             "https://media.giphy.com/media/uqSU9IEYEKAbS/giphy.gif?cid=790b7611lhx31p98zky2l4h82wcxy0ojuvni1wbpdcq8psx4&ep=v1_gifs_search&rid=giphy.gif&ct=g",
             "https://media.giphy.com/media/u8maN0dMhVWPS/giphy.gif?cid=790b7611lhx31p98zky2l4h82wcxy0ojuvni1wbpdcq8psx4&ep=v1_gifs_search&rid=giphy.gif&ct=g",
             "https://media.giphy.com/media/Y6c59hTH3TJoA/giphy.gif?cid=ecf05e478dk1k4348bhm8tdx0qdqcd3py81mir9vism63xdw&ep=v1_gifs_search&rid=giphy.gif&ct=g",
             "https://media.giphy.com/media/kcTnqciIflL8c/giphy.gif?cid=ecf05e478dk1k4348bhm8tdx0qdqcd3py81mir9vism63xdw&ep=v1_gifs_search&rid=giphy.gif&ct=g",
             "https://media.giphy.com/media/RrLbvyvatbi36/giphy.gif?cid=ecf05e478dk1k4348bhm8tdx0qdqcd3py81mir9vism63xdw&ep=v1_gifs_search&rid=giphy.gif&ct=g"]

kiss_gifs = ["https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZjI0ZG1sY21pa25xZnlsOTN6bGF1Y3gyZWs3Mmk4d2t3eTM3NDBtbyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/lTQF0ODLLjhza/giphy.gif",
             "https://media.giphy.com/media/9G0AdBbVrkV3O/giphy.gif?cid=790b7611f24dmlcmiknqfyl93zlaucx2ek72i8wkwy3740mo&ep=v1_gifs_search&rid=giphy.gif&ct=g",
             "https://media.giphy.com/media/Vi0Ws3t4JSLOgdkaBq/giphy.gif?cid=790b7611n9h2eh5uo8gxkgj0ndt7vvzksxvq3cxssreihv67&ep=v1_gifs_search&rid=giphy.gif&ct=g",
             "https://media.giphy.com/media/bCY7hoYdXmD4c/giphy.gif?cid=ecf05e47iogpmr6o0pbt388lulouq5x0s0uydcbk5dck8sav&ep=v1_gifs_search&rid=giphy.gif&ct=g",
             "https://media.giphy.com/media/124gj4XvM8f3fa/giphy.gif?cid=ecf05e47iogpmr6o0pbt388lulouq5x0s0uydcbk5dck8sav&ep=v1_gifs_search&rid=giphy.gif&ct=g",
             "https://media.giphy.com/media/XvES1qJt60SrUf1MzF/giphy.gif?cid=ecf05e47ykq02nc7krgq0355h6r0z433j6l5ut7gtg5jeigx&ep=v1_gifs_search&rid=giphy.gif&ct=g",
             "https://media.giphy.com/media/85gOm7p1lTXob8Qb2b/giphy.gif?cid=ecf05e475pf01jb8p37aeap3m9aag6xbejp4ze0pbnlmv3m5&ep=v1_gifs_search&rid=giphy.gif&ct=g"]

hug_gifs = ["https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZ3o1Y2EyajNjd29kNzg5YTJpZ3lyZnRtbzlhNWxqeHd2aXFrMTBiMCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Vz58J8shFW6BvqnYTm/giphy.gif",
            "https://media.giphy.com/media/9d3LQ6TdV2Flo8ODTU/giphy.gif?cid=790b7611gz5ca2j3cwod789a2igyrftmo9a5ljxwviqk10b0&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            "https://media.giphy.com/media/42YlR8u9gV5Cw/giphy.gif?cid=790b7611gz5ca2j3cwod789a2igyrftmo9a5ljxwviqk10b0&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            "https://media.giphy.com/media/llmZp6fCVb4ju/giphy.gif?cid=790b7611gz5ca2j3cwod789a2igyrftmo9a5ljxwviqk10b0&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            "https://media.giphy.com/media/gnXG2hODaCOru/giphy.gif?cid=ecf05e47w30jdpi5gqp9r4lde9txkgmjj29dqdato4sz3s7l&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            "https://media.giphy.com/media/3oEhmDMA4r9GxhwEqA/giphy.gif?cid=ecf05e4756etlhffisasvdzjc2mq05rb05d22vltkmzodhlq&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            "https://media.giphy.com/media/qCT06WLJURMyfsEi2r/giphy.gif?cid=ecf05e4756etlhffisasvdzjc2mq05rb05d22vltkmzodhlq&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            "https://media.giphy.com/media/l41YkxvU8c7J7Bba0/giphy.gif?cid=ecf05e4756etlhffisasvdzjc2mq05rb05d22vltkmzodhlq&ep=v1_gifs_search&rid=giphy.gif&ct=g"]

pat_gifs = ["https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTE1c2ttdzdpZ2tnczdxNGhnaGI2cDl2YzYycGl6eW91anBqZG1hOCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/N0CIxcyPLputW/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZTE1c2ttdzdpZ2tnczdxNGhnaGI2cDl2YzYycGl6eW91anBqZG1hOCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/lOaf0LBA2mluwm8cY8/giphy.gif",
            "https://media.giphy.com/media/xUA7bahIfcCqC7S4qA/giphy.gif?cid=790b7611e15skmw7igkgs7q4hghb6p9vc62pizyoujpjdma8&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            "https://media.giphy.com/media/3o6Zt2qh8vSNFH30SQ/giphy.gif?cid=790b7611e15skmw7igkgs7q4hghb6p9vc62pizyoujpjdma8&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            "https://media.giphy.com/media/POL1zmGim5AbRfzW4w/giphy.gif?cid=790b7611e15skmw7igkgs7q4hghb6p9vc62pizyoujpjdma8&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            "https://media.giphy.com/media/5z9LtxCsFGP82uGfHy/giphy.gif?cid=790b7611e15skmw7igkgs7q4hghb6p9vc62pizyoujpjdma8&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            "https://media.giphy.com/media/L2z7dnOduqEow/giphy.gif?cid=790b7611e15skmw7igkgs7q4hghb6p9vc62pizyoujpjdma8&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            "https://media.giphy.com/media/1hUQ0gtDCH9OBX898q/giphy.gif?cid=790b7611e15skmw7igkgs7q4hghb6p9vc62pizyoujpjdma8&ep=v1_gifs_search&rid=giphy.gif&ct=g"]

high_five_gifs = ["https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnA5OWZrNTB6NmltZ3NkMjkwOGswNjcydW14ZGF5MXpodWliMDFzaiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oEjHV0z8S7WM4MwnK/giphy.gif",
            "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbnA5OWZrNTB6NmltZ3NkMjkwOGswNjcydW14ZGF5MXpodWliMDFzaiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/b5L1Lt3k4hGNDZWVIw/giphy.gif",
            "https://media.giphy.com/media/26ufgSwMRqauQWqL6/giphy.gif?cid=790b7611np99fk50z6imgsd2908k0672umxday1zhuib01sj&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            "https://media.giphy.com/media/sTYSMiIvgR4yUPX4MK/giphy.gif?cid=790b7611np99fk50z6imgsd2908k0672umxday1zhuib01sj&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            "https://media.giphy.com/media/l1ug5sWBCJOOGzN84/giphy.gif?cid=790b7611np99fk50z6imgsd2908k0672umxday1zhuib01sj&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            "https://media.giphy.com/media/7jxq3zVLu7nWg/giphy.gif?cid=ecf05e47oghdbqn7yz1tthbu1efwulexpnt5wt2hhudov0g6&ep=v1_gifs_search&rid=giphy.gif&ct=g",
            "https://media.giphy.com/media/10LNj580n9OmiI/giphy.gif?cid=ecf05e47oghdbqn7yz1tthbu1efwulexpnt5wt2hhudov0g6&ep=v1_gifs_search&rid=giphy.gif&ct=g"]

poke_gifs = ["https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDZheWtjYmhvdnJqbWJoeXI0bzZsd25jYmJ3azU1dzJqaHBwaTJ1ZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/PkR8gPgc2mDlrMSgtu/giphy.gif",
             "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExcDZheWtjYmhvdnJqbWJoeXI0bzZsd25jYmJ3azU1dzJqaHBwaTJ1ZSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/Vfie0DJryAde8/giphy.gif",
             "https://media.giphy.com/media/uB5zE3KEU5pzMOXM1J/giphy.gif?cid=790b7611p6aykcbhovrjmbhyr4o6lwncbbwk55w2jhppi2ue&ep=v1_gifs_search&rid=giphy.gif&ct=g",
             "https://media.giphy.com/media/uB5zE3KEU5pzMOXM1J/giphy.gif?cid=790b7611p6aykcbhovrjmbhyr4o6lwncbbwk55w2jhppi2ue&ep=v1_gifs_search&rid=giphy.gif&ct=g",
             "https://media.giphy.com/media/aZSMD7CpgU4Za/giphy.gif?cid=790b7611p6aykcbhovrjmbhyr4o6lwncbbwk55w2jhppi2ue&ep=v1_gifs_search&rid=giphy.gif&ct=g",
             "https://media.giphy.com/media/0H0xhd3taWF2RLGtIE/giphy.gif?cid=790b7611p6aykcbhovrjmbhyr4o6lwncbbwk55w2jhppi2ue&ep=v1_gifs_search&rid=giphy.gif&ct=g"]

wink_gifs = ["https://media.giphy.com/media/3o7TKOCXul7Xc8ZBNS/giphy.gif?cid=790b76117oyd729mqcxmfy91gmvjqvcp65179d29oexdqd4i&ep=v1_gifs_search&rid=giphy.gif&ct=g",
             "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExN295ZDcyOW1xY3htZnk5MWdtdmpxdmNwNjUxNzlkMjlvZXhkcWQ0aSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/BI3bNv1NJMC7YzatXd/giphy.gif",
             "https://media.giphy.com/media/12kFpziiPAVYTC/giphy.gif?cid=790b76117oyd729mqcxmfy91gmvjqvcp65179d29oexdqd4i&ep=v1_gifs_search&rid=giphy.gif&ct=g",
             "https://media.giphy.com/media/ncjPKI4JFEL6ePbcxH/giphy.gif?cid=ecf05e47zl4xerwp9lfkyqt64wgzf77trlh7az6arzrd098k&ep=v1_gifs_search&rid=giphy.gif&ct=g",
             "https://media.giphy.com/media/BPHyldtsHgT4VxOLJG/giphy.gif?cid=ecf05e47zl4xerwp9lfkyqt64wgzf77trlh7az6arzrd098k&ep=v1_gifs_search&rid=giphy.gif&ct=g",
             "https://media.giphy.com/media/1pK9NBqJVjU7m/giphy.gif?cid=ecf05e47zl4xerwp9lfkyqt64wgzf77trlh7az6arzrd098k&ep=v1_gifs_search&rid=giphy.gif&ct=g",
             "https://media.giphy.com/media/K7EQ8M8TnuBby/giphy.gif?cid=ecf05e47ypfuleod1a4g11jggdnipeqdx6qdtkkh8hvy254r&ep=v1_gifs_search&rid=giphy.gif&ct=g"]

greet_gifs = ["https://media.giphy.com/media/xBPqJfbMVHoWs/giphy.gif?cid=790b7611szwqw5nt76dwhamnsc7tay0ygxv3as6jg32eq3wb&ep=v1_gifs_search&rid=giphy.gif&ct=g",
              "https://media.giphy.com/media/AuKXmS85YAwcCYexAa/giphy.gif?cid=790b7611szwqw5nt76dwhamnsc7tay0ygxv3as6jg32eq3wb&ep=v1_gifs_search&rid=giphy.gif&ct=g",
              "https://media.giphy.com/media/l1J3uj0ulRPzrHmCY/giphy.gif?cid=790b7611szwqw5nt76dwhamnsc7tay0ygxv3as6jg32eq3wb&ep=v1_gifs_search&rid=giphy.gif&ct=g",
              "https://media.giphy.com/media/Z9hnT4PsD3fwisOfHP/giphy.gif?cid=790b7611szwqw5nt76dwhamnsc7tay0ygxv3as6jg32eq3wb&ep=v1_gifs_search&rid=giphy.gif&ct=g",
              "https://media.giphy.com/media/3ov9jJeIHPhRSlZCgw/giphy.gif?cid=790b7611szwqw5nt76dwhamnsc7tay0ygxv3as6jg32eq3wb&ep=v1_gifs_search&rid=giphy.gif&ct=g",
              "https://media.giphy.com/media/hqArfX7eI7WYEZPNqw/giphy.gif?cid=ecf05e47e3p0h0j053yu82q0gw58jskwj7s7qyo69sv13zed&ep=v1_gifs_search&rid=giphy.gif&ct=g",
              "https://media.giphy.com/media/sYMuExMXbGhovyzJRZ/giphy.gif?cid=ecf05e477wnudiksozoesnos41rfzlon0a0v8ye7holl3jbv&ep=v1_gifs_search&rid=giphy.gif&ct=g"]

kiss_descriptions = [
    "**Oh la la! {} just showered {} with kisses like confetti on New Year's Eve! 💋🎉**",
    "**Smackeroo! {} planted a kiss on {}'s cheek that's sweeter than a candy store on Valentine's Day! 😘🍬**",
    "**Pucker up! {} laid a smooch on {} that's so romantic, it could be a scene in a cheesy rom-com! 💖😍**",
    "**Mwah! {} blew {} a kiss so enchanting, it's like a fairytale come to life! 😚✨**",
    "**Kiss-a-palooza! {} and {} shared a smoochfest so epic, it deserves its own fireworks show! 💥💏**",
    "**Swoon! {} stole {}'s breath away with a kiss so magical, it's like a spell from a love potion! 💫💋**",
    "**Cherish this moment! {} and {} locked lips in a kiss so tender, it's like a scene from a romance novel! 💏📖**",
    "**Mwahahaha! {} planted a kiss on {}'s cheek so mischievous, it's like something out of a cheeky sitcom! 😈💋**",
    "**Kiss attack! {} showered {} with smooches so rapid, it's like a blitz from a squad of affectionate cupids! 😘❤️**",
    "**XOXO! {} and {} shared a kiss so dreamy, it's like a scene from a fairy tale ending! 💋✨**",
]

slap_descriptions = [
"**Oh snap! {} just slapped {} into next Tuesday! 🤚📅**",
"**Bam! {} just delivered a slap so epic, it's echoing in {}'s dreams! 😂💥**",
"**Incoming! {} just launched a slap missile directly at {}'s cheek! 🚀🤚**",
"**Kapow! {} just administered a virtual reality check to {} with that slap! 😆🤚**",
"**Wham! {} just slapped {} with the force of a thousand laughter-inducing memes! 🤚😂**",
"**Zing! {} just unleashed a slap so swift, it broke the sound barrier on its way to {}'s face! 🤚💨**",
"**Ka-chow! {} just slapped {} with the intensity of a thousand electrified rubber bands! ⚡🤚**",
"**Crack! {} just gave {} a virtual high-five...to the face! 🤚🤕**",
"**Boom! {} just dropped a slap bomb on {} that'll be remembered for generations! 💣🤚**",
"**Kaboom! {} just unleashed a slap so powerful, it caused a ripple in the space-time continuum! 🤚🌀😆**",]

hug_descriptions = [
    "**Group hug! {} wraps {} in a warm, fuzzy embrace! 🤗💕**",
    "**Bear hug incoming! {} squeezes {} tightly with love! 🐻💖**",
    "**Hug alert! {} envelopes {} in a comforting hug that melts all worries away! 🚨💞**",
    "**Sending virtual hugs! {} reaches out to {} with arms wide open! 💌🤗**",
    "**Hug-o-meter off the charts! {} and {} share a hug so heartwarming, it could power a small city! 💖🔋**",
    "**Hug time! {} and {} embrace each other with such warmth, even marshmallows feel jealous! 🕒🤗**",
    "**Big squeeze! {} gives {} a hug so tight, it's like a warm blanket on a cold night! 🛌🤗**",
    "**Hug attack! {} ambushes {} with a surprise hug that's sweeter than a basket of puppies! 🎉🐶**",
    "**Snuggle alert! {} cozies up to {} for a cuddle so cozy, even kittens are jealous! 🚨🐱**",
    "**Hugs incoming! {} and {} share a hug so pure, it could rival the softness of freshly baked cookies! 🍪🤗**",
]

pat_descriptions = [
    "**Pat on the back! {} gives {} a friendly pat to show appreciation! 👏🏼😊**",
    "**Gentle pat! {} softly pats {} on the back, spreading good vibes! 🤝💫**",
    "**Comforting pat! {} offers {} a reassuring pat to brighten their day! 🌟🤗**",
    "**Friendly pat! {} gives {} a pat on the shoulder as a sign of friendship! 👋🏼😄**",
    "**Encouraging pat! {} pats {} on the back, cheering them on to victory! 🏆👏🏼**",
    "**Congratulatory pat! {} gives {} a pat on the back for a job well done! 🎉👍🏼**",
    "**Supportive pat! {} offers {} a comforting pat to lift their spirits! 💖🤝**",
    "**Proud pat! {} pats {} on the back with pride, celebrating their success! 🥇🎊**",
    "**Appreciative pat! {} gives {} a pat on the back to show gratitude! 🙏🏼😊**",
    "**Friendly pat! {} pats {} on the shoulder, spreading positivity! 🤗✨**",
]

high_five_descriptions = [
    "**High five! {} and {} share a triumphant high five! 🙌🏼✨**",
    "**Powerful high five! {} and {} slap hands with the force of a thousand suns! ☀️💥**",
    "**Epic high five! {} and {} exchange a high five so legendary, it echoes for miles! 🎤🔊**",
    "**Perfect high five! {} and {} synchronize their hand movements for a flawless high five! 🎯🙌🏼**",
    "**Dynamic duo! {} and {} team up for a high five that's out of this world! 🚀🌟**",
    "**Celebratory high five! {} and {} celebrate victory with an enthusiastic high five! 🏆🙌🏼**",
    "**Fantastic high five! {} and {} slap hands in a display of friendship and camaraderie! 👫👏🏼**",
    "**High five alert! {} and {} raise their hands for an electrifying high five! ⚡️🙌🏼**",
    "**Legendary high five! {} and {} create a moment of pure magic with their high five! ✨🙏🏼**",
    "**High five extravaganza! {} and {} exchange multiple high fives in rapid succession! 🎉🙌🏼**",
]

poke_descriptions = [
    "**Poke alert! {} playfully pokes {}, eliciting a giggle! 😄👉**",
    "**Boop! {} gives {} a gentle poke on the nose! 👃💫**",
    "**Poke attack! {} sneakily pokes {} from behind, causing a surprised reaction! 😯👈**",
    "**Finger poke! {} lightly taps {} with a finger, making them smile! 😊👆**",
    "**Surprise poke! {} unexpectedly pokes {}, resulting in a playful reaction! 😜👈**",
    "**Friendly poke! {} gives {} a friendly poke on the arm, signaling a hello! 👋😄**",
    "**Sneaky poke! {} stealthily pokes {} and then quickly retreats with a grin! 😏👉**",
    "**Gentle poke! {} softly pokes {}, showing affection in a subtle way! 💖👈**",
    "**Poke alert! {} extends a finger and pokes {} gently on the shoulder! 😊👉**",
    "**Tickle poke! {} playfully pokes {} and then pretends it was just a tickle! 😄👈**",
]

wink_descriptions = [
    "**Wink alert! 😉 {} winks at {}, as if to say 'You're my favorite chaos!' 😜**",
    "**Cheeky wink! 😉 {} winks at {}, secretly plotting to steal all the snacks! 🍪😉**",
    "**Sly wink! 😉 {} gives {} a wink, hinting at a conspiracy involving pizza! 🍕😉**",
    "**Friendly wink! 😉 {} winks at {}, inviting them to join the secret handshake club! 🤝😄**",
    "**Flirty wink! 😉 {} sends {} a wink, with a sparkle that says 'Let's taco 'bout love!' 🌮💖**",
    "**Confident wink! 😉 {} winks at {}, revealing the secret to world domination: puppy cuddles! 🐶😎**",
    "**Subtle wink! 😉 {} gives {} a discreet wink, promising adventure and a treasure map to the fridge! 🗺️😉**",
    "**Playful wink! 😉 {} winks at {}, sparking a dance-off where the floor is lava! 💃🕺😄**",
    "**Charming wink! 😉 {} dazzles {} with a wink, as if to say 'You're the marshmallow in my cocoa!' ☕🍫😊**",
    "**Wink of approval! 😉 {} winks at {}, granting them VIP access to the cloud kingdom of pillow forts! ☁️🏰😉**",
]

greeting_descriptions = [
    "**Warm greetings! 🌟 {} welcomes {} with open arms and a heart full of sunshine! ☀️😊**",
    "**Radiant hello! 🌻 {} greets {} with a smile that could light up the night sky! 🌌😄**",
    "**Friendly hello! 👋 {} waves hello to {}, spreading kindness like confetti! 🎉😊**",
    "**Joyous greetings! 🎈 {} showers {} with balloons of happiness and hugs of joy! 🎈🤗**",
    "**Cheery hello! 😊 {} beams at {}, making the world a brighter place with their smile! ✨😄**",
    "**Wholesome welcome! 🌈 {} greets {} with a rainbow of positivity and a sprinkle of magic! 🌈✨**",
    "**Heartfelt hello! ❤️ {} embraces {} with a warm hug and a genuine smile! 🤗😊**",
    "**Kind greeting! 🌼 {} welcomes {} with kindness and compassion, making them feel right at home! 🏡😊**",
    "**Sunny salutations! 🌞 {} greets {} with sunshine-filled smiles and laughter in the air! 🌈😄**",
    "**Bubbly hello! 🎉 {} welcomes {} with bubbles of joy and laughter that never ends! 💖😊**",
]

@bot.command()
async def slap(ctx: commands.Context, user: discord.Member):
    gif = random.choice(slap_gifs)
    description = random.choice(slap_descriptions).format(ctx.author.mention, user.mention)
    color = discord.Color.random()
    
    embed = discord.Embed(
        title="SLAP ATTACK!",
        description=description,
        color=color
    )
    embed.set_image(url=gif)
    embed.set_footer(text="Made by blam")
    
    await ctx.reply(embed=embed)

@bot.command()
async def kiss(ctx: commands.Context, user: discord.Member):
    gif = random.choice(kiss_gifs)
    description = random.choice(kiss_descriptions).format(ctx.author.mention, user.mention)
    color = discord.Color.random()
    embed = discord.Embed(
        title="💋 SMOOCH 💋",
        description=description,
        color=color
    )
    embed.set_image(url=gif)
    embed.set_footer(text="Made by blam")
    
    await ctx.reply(embed=embed)

@bot.command()
async def hug(ctx: commands.Context, user: discord.Member):
    gif = random.choice(hug_gifs)
    description = random.choice(hug_descriptions).format(ctx.author.mention, user.mention)
    color = discord.Color.random()
    embed = discord.Embed(
        title="HUG!!!",
        description=description,
        color=color
    )
    embed.set_image(url=gif)
    embed.set_footer(text="Made by blam")
    
    await ctx.reply(embed=embed)

@bot.command()
async def pat(ctx: commands.Context, user: discord.Member):
    gif = random.choice(pat_gifs)
    description = random.choice(pat_descriptions).format(ctx.author.mention, user.mention)
    color = discord.Color.random()
    embed = discord.Embed(
        title="🎈 Pats of Joy! 🎈",
        description=description,
        color=color
    )
    embed.set_image(url=gif)
    embed.set_footer(text="Made by blam")
    
    await ctx.reply(embed=embed)

@bot.command()
async def high_five(ctx: commands.Context, user: discord.Member):
    gif = random.choice(high_five_gifs)
    description = random.choice(high_five_descriptions).format(ctx.author.mention, user.mention)
    color = discord.Color.random()
    embed = discord.Embed(
        title="🌟 Epic High Five 🌟",
        description=description,
        color=color
    )
    embed.set_image(url=gif)
    embed.set_footer(text="Made by blam")
    
    await ctx.reply(embed=embed)

@bot.command()
async def poke(ctx: commands.Context, user: discord.Member):
    gif = random.choice(poke_gifs)
    description = random.choice(poke_descriptions).format(ctx.author.mention, user.mention)
    color = discord.Color.random()
    embed = discord.Embed(
        title="Poke... 👉",
        description=description,
        color=color
    )
    embed.set_image(url=gif)
    embed.set_footer(text="Made by blam")
    
    await ctx.reply(embed=embed)

@bot.command()
async def wink(ctx: commands.Context, user: discord.Member):
    gif = random.choice(wink_gifs)
    description = random.choice(wink_descriptions).format(ctx.author.mention, user.mention)
    color = discord.Color.random()
    embed = discord.Embed(
        title="Wink Alert! 😉",
        description=description,
        color=color
    )
    embed.set_image(url=gif)
    embed.set_footer(text="Made by blam")
    
    await ctx.reply(embed=embed)

@bot.command()
async def welcome(ctx: commands.Context, user: discord.Member):
    gif = random.choice(greet_gifs)
    description = random.choice(greeting_descriptions).format(ctx.author.mention, user.mention)
    color = discord.Color.random()
    embed = discord.Embed(
        title="WELCOME",
        description=description,
        color=color
    )
    embed.set_image(url=gif)
    embed.set_footer(text="Made by blam")
    
    await ctx.reply(embed=embed)