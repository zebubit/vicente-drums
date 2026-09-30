# Gera index.html (pt), en/index.html e es/index.html a partir de um modelo só.
# Edite os textos em T e rode: python3 build.py
import os, urllib.parse

WA = "5553999973944"
SITE = "https://vicentedrums.com.br/"

T = {
"pt": dict(
 lang="pt-BR", title="Vicente, aquele que vence",
 desc="A história do Vicente, o mini baterista de Rio Grande (RS): da UTI aos 7 meses até as baquetas. Jesus devolveu a vida a ele.",
 seguir="Seguir", sobre="Um testemunho vivo · Rio Grande, RS", sub="aquele que vence",
 fala="“Oi, eu sou o Vicente, e hoje vou tocar uma música pra vocês!”", rolar="Role e conheça a história",
 c1n="Capítulo um", c1t="O resultado das orações",
 c1p1="Antes de ter baquetas, o Vicente já tinha ritmo. Ele mesmo conta: foi crescendo e ficando gordinho na barriga da mamãe Daniele, dava muitos chutinhos de amor pro papai Francisco e <strong>amava ouvir música</strong>.",
 c1p2="Em outubro de 2023 ele chegou, <strong>cem por cento sadio</strong>. Nenhum sinal, nenhum susto. E desde então, nas palavras da família, ele é",
 c1q="a realização de um sonho, o resultado das orações e o amor da vida dos papais.",
 c2n="Capítulo dois", c2t="A chegada",
 c2p="Depois de dois dias no oxigênio, o Vicente precisou ser entubado em um pronto atendimento, que não era o lugar propício para isso. Ele precisava de um leito de UTI para ser transferido, mas o único hospital com UTI pediátrica estava enfrentando uma enchente. Não havia UTI móvel na cidade, nem leito. Depois de algumas horas, a família conseguiu um leito em uma cidade vizinha e também uma ambulância.",
 l1b="Uma semana na UTI", l1="Os exames diziam que não havia mais vírus no corpo do Vicente, mas ele ainda não conseguia respirar sozinho.",
 l2b="Sem diagnóstico", l2="Depois de passar por diversos especialistas, ele simplesmente não tinha diagnóstico. A fala do médico foi: “não podemos mais entubar, as vias aéreas estão comprometidas. Infelizmente, se não houver melhora nos próximos dias, ele pode chegar a uma parada respiratória e precisar de uma traqueostomia.”",
 l3b="O propósito", l3="Sem entender por que estavam vivendo aquilo, os pais resolveram perguntar ao único que poderia responder. Entraram em um propósito de 3 dias de jejum. Naquela noite, lendo a Palavra de Deus, o Senhor falou com eles: no livro de Ester, pediu que entregassem o Vicente nas mãos dele e entendessem que ele não era deles. Foram 3 dias em que a mãe abriu mão das notícias dos médicos e da poltrona ao lado do leito para clamar ao Senhor, enquanto o pai orava de lá. Deus trabalhou nos corações deles e, sem saber, o Espírito Santo os conduziu a dizer: que fosse feita a vontade do Senhor. Se ele curasse o Vicente, continuariam adorando. Se resolvesse levá-lo, continuariam adorando também, porque entendiam que a vontade dele é boa, perfeita e agradável, mesmo quando não a entendem.",
 resp="inspira · expira",
 med="“Não sabemos como ele respirou até os sete meses. <em>Ele é um milagre.</em>”", medc="O que a família ouviu dos médicos",
 c3n="Capítulo três", c3t="E saiu de lá curado",
 c3p1="Depois de 2 dias de propósito, os pais foram chamados para conversar com o médico. As palavras dele: “por mais que ele não tenha condições de ser transferido, o banco de leitos exige que ele seja transferido para a cidade da família.”",
 c3p2="Sabendo que Deus estava no controle de tudo, assinaram os termos. Em seguida a equipe chegou para levá-lo, e uma das médicas pediu que a mãe se sentasse na maca. Sem entender, ela obedeceu. Eles tiraram todos os aparelhos do Vicente e o entregaram no colo dela. <strong>Naquele momento o Senhor respondeu:</strong> com aquele ato, falou com a família que estava devolvendo a vida ao Vicente.",
 c3p3="As lágrimas foram incontroláveis. Das médicas, a família ouviu: “não sei por que fizemos isso, nem poderíamos.” E a mãe respondeu: “vocês foram usadas por Deus para me trazer a resposta.”",
 c3p4="Ao chegar à cidade da família, o Vicente foi avaliado por mais dois otorrinos. Um não tinha resposta, mas o último disse: “não sabemos como o Vicente respirou por 7 meses, ele é um milagre.” Deus os levou àquele hospital porque queria gerar neles um testemunho.",
 c3p5="Ainda não havia melhora alguma e os riscos eram os mesmos, mas tinham a certeza de que ele viveria. Foram transferidos e passaram por duas cirurgias, e a mão do Senhor esteve em cada uma delas.",
 c3p6="A cada retorno, entendem que o procedimento não é permanente e que, a qualquer momento, as vias aéreas dele podem fechar e ocorrer uma parada respiratória. Mas entendem também que é o Senhor quem dá cada suspiro, cada pulsar do pulmão, e a respiração dele continua perfeita.",
 c3q="“Glória a um Deus que faz milagres.”", c3qs="Legenda do testemunho, 11 de outubro de 2024",
 vid="Assista ao testemunho com som", vidalt="Vídeo do testemunho: do hospital aos primeiros passos",
 vir1="Afinal, o Vicente respira", vir2="para a glória de Deus.",
 c4n="Capítulo quatro", c4t="Um ano de vida devolvida",
 c4p1="No dia 8 de outubro de 2024, o Vicente completou 1 ano de vida. No dia 11 de outubro de 2024, a família compartilhou pela primeira vez “um pouquinho do testemunho vivo que é o Vicente”. Nos comentários, uma pergunta se repetia: <strong>o que ele teve?</strong> A resposta está nesta página.",
 c4p2="E dali em diante vieram os balões, os sorrisos, os primeiros passos e, claro, a primeira bateria.",
 ant="Foto anterior", prox="Próxima foto",
 c5n="Capítulo cinco", c5t="Deus: “Vou te dar um talento.”<br>Vicente: “Amém!”",
 c5p1="Desde antes do hospital, os pais percebiam que o Vicente amava mini tambores, baquetas, o barulho de portas batendo e de talheres batendo no prato. Amava bater as mãozinhas e vivia de olho na bateria nos cultos.",
 c5p2="Um mês depois do hospital, em um culto, a família recebeu uma palavra: <strong>“Deus colocou sobre as mãos do Vicente o dom de tocar bateria. Ele não vai precisar de aulas ou de professores. Quando ele tocar, as pessoas vão sentir algo diferente. O que Deus derramou sobre ele é celestial.”</strong>",
 c5p3="Hoje, a brincadeira que o Vicente mais ama é tocar bateria. Em qualquer lugar, com qualquer objeto, ele monta uma bateria e sai tocando, inclusive na escola com os colegas: ele influencia a turma toda a montar uma banda, pegar baquetas e transformar potes, pratos e tudo que encontrar em bateria.",
 t1b="1 aninho", t1="Ganhou do vovô uma bateria de plástico. O resultado surpreendeu todo mundo.",
 t2b="2 aninhos", t2="Ganhou uma bateria eletrônica. E fez por merecer, porque o dom era incrível.",
 t3b="Hoje", t3="O papai e o tio são cantores gospel, e o Vicente já toca nos eventos deles. A cada dia mostra mais experiência e já está sendo convidado para tocar em outros estados do país.",
 c5q="“Instrumento nas mãos do Criador.”",
 fotofinal="Vicente sorrindo, sentado diante de uma bateria azul-turquesa, com balões prateados e azuis ao fundo",
 c6n="Capítulo seis", c6t="Uma família que não para de crescer", mil="mil",
 c6p="de pessoas acompanham hoje o mini baterista. Quando chegou nos 100 mil, a família escreveu que cada passo dá um friozinho na barriga, <strong>sabendo que o Senhor cumpre suas promessas</strong>.",
 notk="Virou notícia", not_="“Pai ensina o filho a tocar bateria, momento emocionante encanta a internet.”",
 rn="Pra assistir com o som ligado", rt="O Vicente tocando", rp="Toque em um vídeo para assistir no Instagram.",
 r1="Ativa o som!", r2="Ensaiando a música do papai pela primeira vez", r3="Te adorar é o que nos sustenta de pé",
 r4="Em gratidão a Deus pelos 100 mil", r5="A chama: o mini baterista ama essa", r6="Com 2 aninhos e 11 meses, acompanhando o papai na agenda",
 kn="Convites", kt="Leve o Vicente para o seu evento ou igreja",
 kp="O Vicente toca ao lado do papai e do tio, cantores gospel. Cultos, congressos, eventos e festas, inclusive em outros estados.",
 k1="Cultos", k2="Congressos", k3="Eventos gospel", k4="Festas",
 kb="Falar com o Francisco", kq="Francisco, pai do Vicente · WhatsApp +55 53 99997-3944",
 kmsg="Olá, Francisco! Vim pelo site do Vicente e quero convidar ele para tocar no meu evento/igreja.",
 pn="Parcerias", pt="Sua marca combina com essa história?", pp="Mais de 101 mil pessoas acompanham o Vicente. Se você quer fechar uma parceria, a conversa é direta com os pais dele.", pc1t="Conteúdo no Instagram", pc1p="Vídeos e stories do Vicente com o seu produto ou a sua mensagem, feitos junto com os pais.", pc2t="Bateria e música", pc2p="Baquetas, pratos, baterias infantis e acessórios para quem está começando a tocar.", pc3t="Produtos infantis", pc3p="Roupas, brinquedos, material escolar e tudo o que faz parte do dia a dia de uma criança.", pc4t="Outra ideia?", pc4p="Se a sua proposta não está aqui, conte para a gente. Toda conversa é bem-vinda.", pb="Propor uma parceria", pmsg="Olá, Francisco! Vim pelo site do Vicente e quero conversar sobre uma parceria com a minha marca.",
 hn="Hoje", ver="Aquele que começou a boa obra <em>é fiel</em> para completá-la.", ref="Filipenses 1:6",
 hp="“Estamos vivendo com o Vicente o que, há mais de um ano, o Senhor disse que viveríamos.” A história continua sendo escrita a cada música, a cada culto, a cada respiração.",
 som1="Ouça o Vicente tocando", som2="com o papai no violão", pausar="Pausar",
 acomp="Acompanhe o Vicente", voltar="Voltar ao início", dev="Desenvolvido por Zebubit Assessoria",
),
"en": dict(
 lang="en", title="Vicente, the one who overcomes",
 desc="The story of Vicente, the little drummer from Rio Grande, Brazil: from the ICU at 7 months old to the drumsticks. Jesus gave him his life back.",
 seguir="Follow", sobre="A living testimony · Rio Grande, Brazil", sub="the one who overcomes",
 fala="“Hi, I'm Vicente, and today I'm going to play a song for you!”", rolar="Scroll to read his story",
 c1n="Chapter one", c1t="The answer to prayers",
 c1p1="Before he ever held drumsticks, Vicente already had rhythm. As he tells it: he grew chubby in mommy Daniele's belly, gave daddy Francisco lots of loving little kicks and <strong>loved listening to music</strong>.",
 c1p2="In October 2023 he arrived, <strong>perfectly healthy</strong>. No signs, no scares. And ever since, in his family's words, he is",
 c1q="a dream come true, the answer to our prayers and the love of his parents' lives.",
 c2n="Chapter two", c2t="The arrival",
 c2p="After two days on oxygen, Vicente had to be intubated at an urgent care clinic, which was not the right place for it. He needed an ICU bed to be transferred, but the only hospital with a pediatric ICU was dealing with the flood. There was no mobile ICU in the city, and no bed. After a few hours, the family found a bed in a neighboring city, and an ambulance too.",
 l1b="A week in the ICU", l1="The tests said there was no more virus in Vicente's body, but he still could not breathe on his own.",
 l2b="No diagnosis", l2="After seeing several specialists, he simply had no diagnosis. The doctor said: “we can't intubate him again, his airways are compromised. Unfortunately, if there is no improvement in the next few days, he may go into respiratory arrest and need a tracheostomy.”",
 l3b="The purpose", l3="Not understanding why they were going through this, his parents decided to ask the only One who could answer. They began a 3-day fast as a purpose before God. That night, reading God's Word, the Lord spoke to them: in the book of Esther, he asked them to place Vicente in his hands and to understand that Vicente was not theirs. For 3 days his mother gave up the doctors' news and the armchair beside his bed to cry out to the Lord, while his father prayed from there. God was working in their hearts and, without knowing it, the Holy Spirit led them to say: let your will be done. If he healed Vicente, they would keep worshiping him. If he chose to take him, they would keep worshiping him too, because they understood that his will is good, perfect and pleasing, even when they don't understand it.",
 resp="breathe in · breathe out",
 med="“We don't know how he breathed until seven months old. <em>He is a miracle.</em>”", medc="What the family heard from the doctors",
 c3n="Chapter three", c3t="And he walked out healed",
 c3p1="After 2 days of this purpose, the parents were called to talk to the doctor. His words: “even though he is not fit to be transferred, the bed registry requires that he be transferred to the family's city.”",
 c3p2="Knowing that God was in control of everything, they signed the papers. Then the team came to take him, and one of the doctors asked his mother to sit on the stretcher. Without understanding why, she obeyed. They removed every device from Vicente and placed him in her lap. <strong>In that moment the Lord answered:</strong> with that act, he told the family that he was giving Vicente's life back.",
 c3p3="The tears were uncontrollable. From the doctors, the family heard: “I don't know why we did this, we shouldn't even be able to.” And his mother replied: “you were used by God to bring me the answer.”",
 c3p4="Back in the family's city, Vicente was seen by two more ENT doctors. One had no answer, but the last one said: “we don't know how Vicente breathed for 7 months, he is a miracle.” God led them to that hospital because he wanted to give them a testimony.",
 c3p5="There was still no improvement and the risks were the same, but they were certain he would live. They were transferred and went through two surgeries, and the hand of the Lord was in every one of them.",
 c3p6="At every follow-up, they understand that the procedure is not permanent and that, at any moment, his airways could close and cause respiratory arrest. But they also understand that it is the Lord who gives every breath, every beat of the lungs, and his breathing remains perfect.",
 c3q="“Glory to a God who does miracles.”", c3qs="Testimony caption, October 11, 2024",
 vid="Watch the testimony with sound", vidalt="Testimony video: from the hospital to his first steps",
 vir1="After all, Vicente breathes", vir2="for the glory of God.",
 c4n="Chapter four", c4t="A year of life given back",
 c4p1="On October 8, 2024, Vicente turned 1 year old. On October 11, 2024, the family shared for the first time “a little of the living testimony that is Vicente”. In the comments, one question kept coming up: <strong>what did he have?</strong> The answer is on this page.",
 c4p2="And from then on came the balloons, the smiles, the first steps and, of course, the first drum set.",
 ant="Previous photo", prox="Next photo",
 c5n="Chapter five", c5t="God: “I'll give you a gift.”<br>Vicente: “Amen!”",
 c5p1="Even before the hospital, his parents noticed that Vicente loved mini drums, drumsticks, the noise of slamming doors and of cutlery clinking on a plate. He loved clapping his little hands and always kept his eyes on the drums at church.",
 c5p2="A month after the hospital, at a church service, the family received a word: <strong>“God placed on Vicente's hands the gift of playing the drums. He will not need lessons or teachers. When he plays, people will feel something different. What God poured out on him is heavenly.”</strong>",
 c5p3="Today, the game Vicente loves most is playing the drums. Anywhere, with any object, he builds a drum set and starts playing, even at school with his classmates: he gets the whole class to form a band, grab drumsticks and turn pots, plates and everything they find into drums.",
 t1b="Age 1", t1="Grandpa gave him a plastic drum set. The result surprised everyone.",
 t2b="Age 2", t2="He got an electronic drum kit. And he earned it, because his gift was amazing.",
 t3b="Today", t3="His dad and his uncle are gospel singers, and Vicente already plays at their events. Every day he shows more experience, and he is already being invited to play in other states across Brazil.",
 c5q="“An instrument in the hands of the Creator.”",
 fotofinal="Vicente smiling, sitting in front of a turquoise drum set, with silver and blue balloons behind him",
 c6n="Chapter six", c6t="A family that keeps growing", mil="K",
 c6p="people follow the little drummer today. When they reached 100K, the family wrote that every step gives them butterflies, <strong>knowing that the Lord keeps His promises</strong>.",
 notk="In the news", not_="“Dad teaches his son to play drums, emotional moment wins over the internet.”",
 rn="Turn the sound on", rt="Vicente playing", rp="Tap a video to watch it on Instagram.",
 r1="Sound on!", r2="Rehearsing daddy's song for the first time", r3="Worshipping You is what keeps us standing",
 r4="Thanking God for 100K", r5="The flame: the little drummer loves this one", r6="At 2 years and 11 months, joining daddy on tour",
 kn="Invitations", kt="Bring Vicente to your event or church",
 kp="Vicente plays alongside his dad and his uncle, who are gospel singers. Church services, conferences, events and celebrations, including in other states.",
 k1="Church services", k2="Conferences", k3="Gospel events", k4="Celebrations",
 kb="Talk to Francisco", kq="Francisco, Vicente's dad · WhatsApp +55 53 99997-3944 (Portuguese)",
 kmsg="Hi Francisco! I found Vicente's website and would like to invite him to play at my event/church.",
 pn="Partnerships", pt="Does your brand fit this story?", pp="More than 101 thousand people follow Vicente. If you'd like to build a partnership, the conversation is direct with his parents.", pc1t="Instagram content", pc1p="Videos and stories with Vicente featuring your product or your message, made together with his parents.", pc2t="Drums and music", pc2p="Drumsticks, cymbals, kids' drum sets and accessories for beginners.", pc3t="Kids' products", pc3p="Clothes, toys, school supplies and everything that is part of a child's daily life.", pc4t="Another idea?", pc4p="If your proposal isn't here, tell us. Every conversation is welcome.", pb="Propose a partnership", pmsg="Hello, Francisco! I came from Vicente's website and I'd like to talk about a partnership with my brand.",
 hn="Today", ver="He who began a good work <em>is faithful</em> to complete it.", ref="Philippians 1:6",
 hp="“We are living with Vicente what the Lord told us, more than a year ago, that we would live.” The story is still being written with every song, every service, every breath.",
 som1="Hear Vicente play", som2="with daddy on guitar", pausar="Pause",
 acomp="Follow Vicente", voltar="Back to top", dev="Built by Zebubit Assessoria",
),
"es": dict(
 lang="es", title="Vicente, el que vence",
 desc="La historia de Vicente, el mini baterista de Rio Grande, Brasil: de la UCI a los 7 meses hasta las baquetas. Jesús le devolvió la vida.",
 seguir="Seguir", sobre="Un testimonio vivo · Rio Grande, Brasil", sub="el que vence",
 fala="“¡Hola, soy Vicente, y hoy voy a tocar una canción para ustedes!”", rolar="Desliza y conoce su historia",
 c1n="Capítulo uno", c1t="La respuesta a las oraciones",
 c1p1="Antes de tener baquetas, Vicente ya tenía ritmo. Él mismo lo cuenta: fue creciendo y poniéndose gordito en la panza de mamá Daniele, le daba muchas pataditas de amor a papá Francisco y <strong>le encantaba escuchar música</strong>.",
 c1p2="En octubre de 2023 llegó, <strong>completamente sano</strong>. Ninguna señal, ningún susto. Y desde entonces, en palabras de su familia, él es",
 c1q="un sueño hecho realidad, la respuesta a las oraciones y el amor de la vida de sus papás.",
 c2n="Capítulo dos", c2t="La llegada",
 c2p="Después de dos días con oxígeno, Vicente tuvo que ser intubado en una sala de urgencias, que no era el lugar adecuado para eso. Necesitaba una cama de UCI para ser trasladado, pero el único hospital con UCI pediátrica estaba enfrentando la inundación. No había UCI móvil en la ciudad, ni cama. Después de algunas horas, la familia consiguió una cama en una ciudad vecina y también una ambulancia.",
 l1b="Una semana en la UCI", l1="Los exámenes decían que ya no había virus en el cuerpo de Vicente, pero todavía no lograba respirar solo.",
 l2b="Sin diagnóstico", l2="Después de pasar por varios especialistas, simplemente no tenía diagnóstico. El médico dijo: “ya no podemos intubarlo, las vías respiratorias están comprometidas. Lamentablemente, si no hay mejoría en los próximos días, puede llegar a un paro respiratorio y necesitar una traqueostomía.”",
 l3b="El propósito", l3="Sin entender por qué estaban viviendo aquello, sus papás decidieron preguntarle al único que podía responder. Entraron en un propósito de 3 días de ayuno. Esa noche, leyendo la Palabra de Dios, el Señor les habló: en el libro de Ester, les pidió que entregaran a Vicente en sus manos y que entendieran que él no era de ellos. Fueron 3 días en que la mamá dejó de lado las noticias de los médicos y el sillón junto a la cama para clamar al Señor, mientras el papá oraba desde allá. Dios trabajó en sus corazones y, sin saberlo, el Espíritu Santo los llevó a decir: que se hiciera su voluntad. Si sanaba a Vicente, seguirían adorándolo. Si decidía llevárselo, también seguirían adorándolo, porque entendían que su voluntad es buena, perfecta y agradable, aun cuando no la entienden.",
 resp="inhala · exhala",
 med="“No sabemos cómo respiró hasta los siete meses. <em>Es un milagro.</em>”", medc="Lo que la familia escuchó de los médicos",
 c3n="Capítulo tres", c3t="Y salió curado",
 c3p1="Después de 2 días de propósito, los papás fueron llamados para hablar con el médico. Sus palabras: “aunque no esté en condiciones de ser trasladado, el banco de camas exige que sea trasladado a la ciudad de la familia.”",
 c3p2="Sabiendo que Dios tenía el control de todo, firmaron los documentos. Enseguida llegó el equipo para llevárselo, y una de las médicas le pidió a la mamá que se sentara en la camilla. Sin entender, obedeció. Le quitaron todos los aparatos a Vicente y se lo entregaron en su regazo. <strong>En ese momento el Señor respondió:</strong> con ese acto, le dijo a la familia que le estaba devolviendo la vida a Vicente.",
 c3p3="Las lágrimas fueron incontrolables. De las médicas escucharon: “no sé por qué hicimos esto, ni siquiera podíamos.” Y la mamá respondió: “ustedes fueron usadas por Dios para traerme la respuesta.”",
 c3p4="Al llegar a la ciudad de la familia, Vicente fue evaluado por dos otorrinos más. Uno no tenía respuesta, pero el último dijo: “no sabemos cómo Vicente respiró durante 7 meses, es un milagro.” Dios los llevó a ese hospital porque quería generar en ellos un testimonio.",
 c3p5="Todavía no había ninguna mejoría y los riesgos eran los mismos, pero tenían la certeza de que viviría. Fueron trasladados y pasaron por dos cirugías, y la mano del Señor estuvo en cada una de ellas.",
 c3p6="En cada control, entienden que el procedimiento no es permanente y que, en cualquier momento, sus vías respiratorias pueden cerrarse y provocar un paro respiratorio. Pero también entienden que es el Señor quien da cada suspiro, cada latido del pulmón, y su respiración sigue siendo perfecta.",
 c3q="“Gloria a un Dios que hace milagros.”", c3qs="Leyenda del testimonio, 11 de octubre de 2024",
 vid="Mira el testimonio con sonido", vidalt="Video del testimonio: del hospital a sus primeros pasos",
 vir1="Al final, Vicente respira", vir2="para la gloria de Dios.",
 c4n="Capítulo cuatro", c4t="Un año de vida devuelta",
 c4p1="El 8 de octubre de 2024, Vicente cumplió 1 año de vida. El 11 de octubre de 2024, la familia compartió por primera vez “un poquito del testimonio vivo que es Vicente”. En los comentarios se repetía una pregunta: <strong>¿qué tuvo?</strong> La respuesta está en esta página.",
 c4p2="Y desde entonces llegaron los globos, las sonrisas, los primeros pasos y, claro, la primera batería.",
 ant="Foto anterior", prox="Foto siguiente",
 c5n="Capítulo cinco", c5t="Dios: “Te voy a dar un talento.”<br>Vicente: “¡Amén!”",
 c5p1="Desde antes del hospital, sus papás notaban que Vicente amaba los mini tambores, las baquetas, el ruido de las puertas al cerrarse y de los cubiertos golpeando el plato. Amaba aplaudir con sus manitas y siempre tenía los ojos puestos en la batería en los cultos.",
 c5p2="Un mes después del hospital, en un culto, la familia recibió una palabra: <strong>“Dios puso sobre las manos de Vicente el don de tocar la batería. No va a necesitar clases ni profesores. Cuando toque, la gente va a sentir algo diferente. Lo que Dios derramó sobre él es celestial.”</strong>",
 c5p3="Hoy, el juego que Vicente más ama es tocar la batería. En cualquier lugar, con cualquier objeto, arma una batería y sale tocando, incluso en la escuela con sus compañeros: contagia a todo el grupo para armar una banda, tomar baquetas y convertir ollas, platos y todo lo que encuentren en una batería.",
 t1b="1 añito", t1="El abuelo le regaló una batería de plástico. El resultado sorprendió a todos.",
 t2b="2 añitos", t2="Recibió una batería electrónica. Y se la ganó, porque su don era increíble.",
 t3b="Hoy", t3="Su papá y su tío son cantantes gospel, y Vicente ya toca en sus eventos. Cada día muestra más experiencia y ya lo invitan a tocar en otros estados de Brasil.",
 c5q="“Instrumento en las manos del Creador.”",
 fotofinal="Vicente sonriendo, sentado frente a una batería turquesa, con globos plateados y azules al fondo",
 c6n="Capítulo seis", c6t="Una familia que no para de crecer", mil="mil",
 c6p="personas siguen hoy al mini baterista. Cuando llegaron a los 100 mil, la familia escribió que cada paso les da mariposas en el estómago, <strong>sabiendo que el Señor cumple sus promesas</strong>.",
 notk="Fue noticia", not_="“Papá enseña a su hijo a tocar batería, un momento emocionante que conquista internet.”",
 rn="Para ver con el sonido activado", rt="Vicente tocando", rp="Toca un video para verlo en Instagram.",
 r1="¡Activa el sonido!", r2="Ensayando la canción de papá por primera vez", r3="Adorarte es lo que nos mantiene de pie",
 r4="En gratitud a Dios por los 100 mil", r5="La llama: al mini baterista le encanta esta", r6="Con 2 añitos y 11 meses, acompañando a papá en la agenda",
 kn="Invitaciones", kt="Lleva a Vicente a tu evento o iglesia",
 kp="Vicente toca junto a su papá y su tío, cantantes gospel. Cultos, congresos, eventos y fiestas, incluso en otros estados.",
 k1="Cultos", k2="Congresos", k3="Eventos gospel", k4="Fiestas",
 kb="Hablar con Francisco", kq="Francisco, papá de Vicente · WhatsApp +55 53 99997-3944 (portugués)",
 kmsg="¡Hola, Francisco! Vi el sitio de Vicente y quiero invitarlo a tocar en mi evento/iglesia.",
 pn="Alianzas", pt="¿Tu marca combina con esta historia?", pp="Más de 101 mil personas siguen a Vicente. Si quieres cerrar una alianza, la conversación es directa con sus papás.", pc1t="Contenido en Instagram", pc1p="Videos e historias de Vicente con tu producto o tu mensaje, hechos junto con sus papás.", pc2t="Batería y música", pc2p="Baquetas, platillos, baterías infantiles y accesorios para quien está empezando a tocar.", pc3t="Productos infantiles", pc3p="Ropa, juguetes, útiles escolares y todo lo que forma parte del día a día de un niño.", pc4t="¿Otra idea?", pc4p="Si tu propuesta no está aquí, cuéntanos. Toda conversación es bienvenida.", pb="Proponer una alianza", pmsg="¡Hola, Francisco! Vine por el sitio de Vicente y quiero conversar sobre una alianza con mi marca.",
 hn="Hoy", ver="El que comenzó la buena obra <em>es fiel</em> para completarla.", ref="Filipenses 1:6",
 hp="“Estamos viviendo con Vicente lo que, hace más de un año, el Señor nos dijo que viviríamos.” La historia se sigue escribiendo en cada canción, cada culto, cada respiración.",
 som1="Escucha a Vicente tocar", som2="con papá en la guitarra", pausar="Pausar",
 acomp="Sigue a Vicente", voltar="Volver al inicio", dev="Desarrollado por Zebubit Assessoria",
),
}

IG = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor"/></svg>'
PLAY = '<div class="play"><svg viewBox="0 0 24 24" fill="#fff"><path d="M8 5v14l11-7z"/></svg></div>'
WAICO = '<svg viewBox="0 0 24 24" fill="currentColor" aria-hidden="true"><path d="M17.5 14.4c-.3-.1-1.8-.9-2-1-.3-.1-.5-.1-.7.1-.2.3-.8 1-.9 1.2-.2.2-.3.2-.6.1-.3-.1-1.3-.5-2.4-1.5-.9-.8-1.5-1.8-1.7-2.1-.2-.3 0-.5.1-.6l.4-.5.3-.5c.1-.2 0-.4 0-.5l-.9-2.2c-.2-.6-.5-.5-.7-.5h-.6c-.2 0-.5.1-.8.4-.3.3-1 1-1 2.5s1.1 2.9 1.2 3.1c.1.2 2.1 3.2 5.1 4.5.7.3 1.3.5 1.7.6.7.2 1.4.2 1.9.1.6-.1 1.8-.7 2-1.4.3-.7.3-1.3.2-1.4-.1-.1-.3-.2-.6-.3zM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2z"/></svg>'

def pagina(k):
    t = T[k]; p = "" if k == "pt" else "../"
    wa = f"https://wa.me/{WA}?text=" + urllib.parse.quote(t["kmsg"])
    wa2 = f"https://wa.me/{WA}?text=" + urllib.parse.quote(t["pmsg"])
    def cur(x): return ' aria-current="true"' if x == k else ''
    reels = [("DA_5eMhvQ2A","testemunho-capa","vid"),("DUUIFPiAQDC","fone-sorriso","r1"),("Da-nTHERC54","papai-violao","r2"),
             ("DXp4K47j1q_","chapeu","r3"),("DdXdqI4P-_u","floresta","r4"),("DdumxbAP5nf","fone-riso","r5"),("DdiBmXzxNul","noite-igreja","r6")]
    reels = reels[1:]
    rh = "".join(f'<a class="reel rv{" d"+str(i%3) if i%3 else ""}" href="https://www.instagram.com/reel/{c}/" target="_blank" rel="noopener"><img src="{p}img/{im}.jpg" alt="" loading="lazy">{PLAY}<span>{t[tx]}</span></a>' for i,(c,im,tx) in enumerate(reels))
    return f'''<!doctype html>
<html lang="{t["lang"]}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{t["title"]}</title>
<meta name="description" content="{t["desc"]}">
<meta property="og:title" content="{t["title"]}">
<meta property="og:description" content="{t["desc"]}">
<meta property="og:image" content="{SITE}img/hero.jpg">
<link rel="alternate" hreflang="pt-BR" href="{SITE}">
<link rel="alternate" hreflang="en" href="{SITE}en/">
<link rel="alternate" hreflang="es" href="{SITE}es/">
<meta name="theme-color" content="#0d0e11">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..800;1,9..144,300..700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{p}style.css">
</head>
<body>
<div class="progresso" id="progresso" aria-hidden="true"></div>
<header class="nav" id="nav">
  <a class="marca" href="#topo">Vicente <em>drums</em></a>
  <div class="nav-dir">
    <nav class="idiomas" aria-label="Idioma / Language">
      <a href="{p}./" hreflang="pt-BR" lang="pt-BR"{cur("pt")}>PT</a><a href="{p}en/" hreflang="en" lang="en"{cur("en")}>EN</a><a href="{p}es/" hreflang="es" lang="es"{cur("es")}>ES</a>
    </nav>
    <a class="btn-ig" href="https://www.instagram.com/vicentedrums_/" target="_blank" rel="noopener">{IG}<span class="txt">{t["seguir"]}</span></a>
  </div>
</header>

<main id="topo">
<section class="hero">
  <div class="hero-img">
    <img class="fundo" src="{p}img/hero.jpg" alt="" aria-hidden="true">
    <img class="foto-hero" src="{p}img/hero.jpg" alt="Vicente" fetchpriority="high">
  </div>
  <div class="wrap hero-txt">
    <p class="sobre rv">{t["sobre"]}</p>
    <h1 class="rv d1">Vicente<span>{t["sub"]}</span></h1>
    <p class="fala rv d2">{t["fala"]}</p>
    <a class="rolar rv d3" href="#sonho"><i></i> {t["rolar"]}</a>
  </div>
</section>

<section class="cap" id="sonho">
  <div class="wrap">
    <div class="duo">
      <div class="rv">
        <p class="num">{t["c1n"]}</p>
        <h2>{t["c1t"]}</h2>
        <p>{t["c1p1"]}</p>
        <p>{t["c1p2"]}</p>
        <p class="citacao">{t["c1q"]}</p>
      </div>
      <div class="foto rv d1" style="aspect-ratio:4/5"><img src="{p}img/gravidez.jpg" alt="" loading="lazy"></div>
    </div>
    <div class="mosaico" style="margin-top:56px">
      <div class="foto rv"><img src="{p}img/nascimento.jpg" alt="" loading="lazy"></div>
      <div class="foto rv d1"><img src="{p}img/papai-berco.jpg" alt="" loading="lazy"></div>
      <div class="foto rv d2"><img src="{p}img/papai-beijo.jpg" alt="" loading="lazy"></div>
    </div>
  </div>
</section>

<div class="escuro">
<section class="cap" id="uti">
  <div class="wrap">
    <div class="duo inv">
      <div class="rv">
        <p class="num">{t["c2n"]}</p>
        <h2>{t["c2t"]}</h2>
        <p>{t["c2p"]}</p>
        <ol class="linha-tempo">
          <li class="rv"><b>{t["l1b"]}</b><span>{t["l1"]}</span></li>
          <li class="rv d1"><b>{t["l2b"]}</b><span>{t["l2"]}</span></li>
          <li class="rv d2"><b>{t["l3b"]}</b><span>{t["l3"]}</span></li>
        </ol>
      </div>
      <div class="foto rv d1" style="aspect-ratio:3/4"><img src="{p}img/uti-dormindo.jpg" alt="" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="medicos">
  <div class="wrap">
    <div class="respiro rv" aria-hidden="true"><div class="pulmao"></div><p>{t["resp"]}</p></div>
    <blockquote class="rv d1">{t["med"]}</blockquote>
    <cite class="rv d2">{t["medc"]}</cite>
  </div>
</section>

<section class="cap" style="padding-top:0">
  <div class="wrap">
    <div class="duo">
      <div class="rv">
        <div class="video-box" id="videoBox">
          <video id="video" src="{p}video/testemunho.mp4" poster="{p}img/testemunho-capa.jpg" preload="none" playsinline aria-label="{t["vidalt"]}"></video>
          <button class="video-play" type="button" id="videoPlay"><span class="circ"><svg viewBox="0 0 24 24" fill="#fff" aria-hidden="true"><path d="M8 5v14l11-7z"/></svg></span><span class="rot">{t["vid"]}</span></button>
        </div>
      </div>
      <div class="rv d1">
        <p class="num">{t["c3n"]}</p>
        <h2>{t["c3t"]}</h2>
        <p>{t["c3p1"]}</p>
        <p>{t["c3p2"]}</p>
        <p>{t["c3p3"]}</p>
        <p>{t["c3p4"]}</p>
        <p>{t["c3p5"]}</p>
        <p>{t["c3p6"]}</p>
        <p class="citacao">{t["c3q"]}<small>{t["c3qs"]}</small></p>
      </div>
    </div>
  </div>
</section>
</div>

<section class="virada">
  <div class="wrap"><h2 class="rv">{t["vir1"]}<strong>{t["vir2"]}</strong></h2></div>
</section>

<section class="cap" id="vida">
  <div class="wrap">
    <div class="estreito rv">
      <p class="num">{t["c4n"]}</p>
      <h2>{t["c4t"]}</h2>
      <p>{t["c4p1"]}</p>
      <p>{t["c4p2"]}</p>
    </div>
    <div class="carrossel rv d1">
      <div class="trilho" id="trilho" tabindex="0">
        <figure><img src="{p}img/um-ano.jpg" alt="" loading="lazy"></figure>
        <figure><img src="{p}img/familia-beijo.jpg" alt="" loading="lazy"></figure>
        <figure><img src="{p}img/um-ano-bolo.jpg" alt="" loading="lazy"></figure>
        <figure><img src="{p}img/mamae-colo.jpg" alt="" loading="lazy"></figure>
        <figure><img src="{p}img/rua.jpg" alt="" loading="lazy"></figure>
        <figure><img src="{p}img/ceu.jpg" alt="" loading="lazy"></figure>
        <figure><img src="{p}img/maos.jpg" alt="" loading="lazy"></figure>
      </div>
      <div class="setas">
        <button type="button" data-dir="-1" aria-label="{t["ant"]}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M15 18l-6-6 6-6"/></svg></button>
        <button type="button" data-dir="1" aria-label="{t["prox"]}"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M9 6l6 6-6 6"/></svg></button>
      </div>
    </div>
  </div>
</section>

<section class="cap" id="baquetas" style="background:var(--papel)">
  <div class="wrap">
    <div class="duo">
      <div class="rv">
        <p class="num">{t["c5n"]}</p>
        <h2>{t["c5t"]}</h2>
        <p>{t["c5p1"]}</p>
        <p>{t["c5p2"]}</p>
        <ol class="linha-tempo clara">
          <li class="rv"><b>{t["t1b"]}</b><span>{t["t1"]}</span></li>
          <li class="rv d1"><b>{t["t2b"]}</b><span>{t["t2"]}</span></li>
          <li class="rv d2"><b>{t["t3b"]}</b><span>{t["t3"]}</span></li>
        </ol>
        <p>{t["c5p3"]}</p>
        <p class="citacao">{t["c5q"]}</p>
      </div>
      <div class="foto rv d1" style="aspect-ratio:3/4"><img src="{p}img/riso-bateria.jpg" alt="" loading="lazy"></div>
    </div>
    <div class="mosaico" style="margin-top:56px">
      <div class="foto rv"><img src="{p}img/papai-violao.jpg" alt="" loading="lazy"></div>
      <div class="foto rv d1"><img src="{p}img/talento.jpg" alt="" loading="lazy"></div>
      <div class="foto rv d2"><img src="{p}img/herval.jpg" alt="" loading="lazy"></div>
    </div>
  </div>
</section>

<section class="cap marcas" id="marcas">
  <div class="wrap">
    <div class="estreito">
      <p class="num rv">{t["c6n"]}</p>
      <h2 class="rv">{t["c6t"]}</h2>
      <div class="contador rv d1" id="contador" data-alvo="101" data-suf="{t["mil"]}">0</div>
      <p class="rv d2">{t["c6p"]}</p>
    </div>
    <div class="degraus">
      <div class="degrau rv"><img src="{p}img/mil.jpg" alt="" loading="lazy"><b>1K</b></div>
      <div class="degrau rv d1"><img src="{p}img/poster-20k.jpg" alt="" loading="lazy"><b>20K</b></div>
      <div class="degrau rv d2"><img src="{p}img/bolo-50k.jpg" alt="" loading="lazy"><b>50K</b></div>
      <div class="degrau rv d3"><img src="{p}img/cem-mil.jpg" alt="" loading="lazy"><b>100K</b></div>
    </div>
    <div class="noticia rv"><small>{t["notk"]}</small><p>{t["not_"]}</p></div>
  </div>
</section>

<section class="cap" id="reels">
  <div class="wrap">
    <div class="estreito rv">
      <p class="num">{t["rn"]}</p>
      <h2>{t["rt"]}</h2>
      <p>{t["rp"]}</p>
    </div>
    <div class="reels">{rh}</div>
  </div>
</section>

<section class="cap contato" id="convite">
  <div class="wrap">
    <p class="num rv">{t["kn"]}</p>
    <h2 class="rv">{t["kt"]}</h2>
    <p class="rv d1">{t["kp"]}</p>
    <ul class="tipos rv d1"><li>{t["k1"]}</li><li>{t["k2"]}</li><li>{t["k3"]}</li><li>{t["k4"]}</li></ul>
    <a class="btn-wa rv d2" href="{wa}" target="_blank" rel="noopener">{WAICO}{t["kb"]}</a>
    <p class="quem rv d2">{t["kq"]}</p>
  </div>
</section>

<section class="cap parc" id="parcerias">
  <div class="wrap">
    <div class="estreito rv">
      <p class="num">{t["pn"]}</p>
      <h2>{t["pt"]}</h2>
      <p>{t["pp"]}</p>
    </div>
    <div class="cards rv d1" tabindex="0">
      <article class="card"><h3>{t["pc1t"]}</h3><p>{t["pc1p"]}</p></article>
      <article class="card"><h3>{t["pc2t"]}</h3><p>{t["pc2p"]}</p></article>
      <article class="card"><h3>{t["pc3t"]}</h3><p>{t["pc3p"]}</p></article>
      <article class="card"><h3>{t["pc4t"]}</h3><p>{t["pc4p"]}</p></article>
    </div>
    <a class="btn-wa rv d2" href="{wa2}" target="_blank" rel="noopener">{WAICO}{t["pb"]}</a>
    <p class="quem-parc rv d2">{t["kq"]}</p>
  </div>
</section>

<section class="cap final" id="hoje">
  <div class="wrap">
    <div class="foto rv"><img src="{p}img/final-bateria.jpg" alt="{t["fotofinal"]}" loading="lazy"></div>
    <p class="num rv">{t["hn"]}</p>
    <p class="versiculo rv d1">{t["ver"]}</p>
    <p class="ref rv d2">{t["ref"]}</p>
    <p class="rv" style="max-width:600px;margin:0 auto 36px;color:var(--tinta2)">{t["hp"]}</p>
    <div class="acoes rv">
      <a class="btn-ig" href="https://www.instagram.com/vicentedrums_/" target="_blank" rel="noopener">{IG}{t["acomp"]}</a>
      <a class="btn-sec" href="#topo">{t["voltar"]}</a>
    </div>
  </div>
</section>
</main>

<footer>
  Vicente Drums · Rio Grande, RS<br>
  <a href="https://zebubit.com.br" target="_blank" rel="noopener">{t["dev"]}</a>
</footer>
<button class="som" id="som" type="button" aria-pressed="false" data-tocar="{t["som1"]}" data-pausar="{t["pausar"]}">
  <span class="ico" aria-hidden="true"><svg class="i-play" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg><span class="barras"><i></i><i></i><i></i><i></i></span></span>
  <span class="txt"><b id="somTxt">{t["som1"]}</b><small>{t["som2"]}</small></span>
</button>
<audio id="audio" src="{p}audio/vicente-tocando.mp3" preload="none"></audio>
<script src="{p}app.js"></script>
</body>
</html>
'''

for k in T:
    out = "index.html" if k == "pt" else f"{k}/index.html"
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    open(out, "w").write(pagina(k))
    print("ok", out)
