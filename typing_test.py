import time
import random
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Success is not final, failure is not fatal: it is the courage to continue that counts.",
    "Coding is the closest thing we have to a superpower in the modern world.",
    "The beautiful thing about learning is that no one can take it away from you.",
    "Artificial intelligence is growing at an unprecedented pace these days.",
    "A journey of a thousand miles begins with a single step.",
    "Please make sure to wash your hands before preparing dinner.",
    "The weather forecast predicts heavy rain and strong winds for tomorrow afternoon.",
    "She sells sea shells by the sea shore on a sunny day.",
    "Patience and perseverance have a magical effect before which difficulties disappear.",
    " can write code that a computer understands, but good programmers write code that humans understand.",
    "The solar system consists of the sun and all the celestial objects bound to it by gravity.",
    "Reading books is a wonderful way to expand your vocabulary and imagination.",
    "The coffee shop on the corner always smells like freshly ground espresso.",
    "Consistency is much more important than perfection when building a new habit.",
    "Light travels at an incredible speed of approximately three hundred thousand kilometers per second.",
    "Don't count the days, make the days count.",
    "The museum featured a stunning collection of ancient artifacts and modern art.",
    "Taking a deep breath can help reduce stress and improve your focus immediately.",
    "The internet has completely transformed the way people communicate and share information.",
    "Practice makes perfect, so keep typing as fast and accurately as you can.",
    "Trees play a crucial role in absorbing carbon dioxide and producing oxygen.",
    "An apple a day keeps the doctor away, or so the old saying goes.",
    "The orchestra played a beautiful symphony that captivated the entire audience.",
    "Learning a new language opens up a whole world of cultural experiences.",
    "The early bird catches the worm, but the second mouse gets the cheese.",
    "Innovation distinguishes between a leader and a follower in any industry.",
    "Mountains look absolutely majestic when the peak is covered in fresh winter snow.",
    "A regular exercise routine can significantly boost your physical and mental health.",
    "Always remember to back up your important computer files to an external drive.",
    "The ocean covers more than seventy percent of the planet's surface.",
    "To be or not to be, that is the ultimate question.",
    "The rapid growth of technology has created many exciting new career paths.",
    "A warm cup of tea on a rainy afternoon is incredibly comforting.",
    "Space exploration helps us understand our place in this vast universe.",
    "Do not go where the path may lead, go instead where there is no path and leave a trail.",
    "Computers process millions of instructions per second without breaking a sweat.",
    "The smell of old books always brings back fond memories of childhood libraries.",
    "Believe you can and you are already halfway there.",
    "Time flies like an arrow, but fruit flies like a banana."
]
paragraphs = [
    "Technology has fundamentally altered the fabric of human existence over the last few decades. What started as basic automation has blossomed into a complex digital ecosystem that governs our daily routines. We rely on smartphones for communication, artificial intelligence for decision-making, and the internet for an infinite stream of information. While these advancements have brought undeniable convenience and connectivity, they also challenge our attention spans and privacy. Striking a healthy balance between the virtual world and physical reality is one of the greatest challenges of modern life. As we move forward, humanity must shape technology mindfully.",
    
    "The cosmos has always captured the human imagination with its vast, silent grandeur. Beyond our tiny blue planet lies an infinite expanse filled with billions of galaxies, each hosting countless stars and mysterious worlds. Astronomers use powerful space telescopes to peer deep into the past, capturing ancient light from the very edge of the observable universe. Every discovery reveals something incredible, from swirling nebulae where new stars are born to massive black holes that distort time itself. Exploring the universe reminds us of how small we are, yet it highlights our unique capacity to wonder, learn, and explore.",
    
    "Reading a well-written book is like stepping into a time machine or opening a portal to another dimension. Without moving a single inch, a reader can experience the bustling streets of ancient Rome, explore distant futuristic planets, or feel the deep emotions of a stranger. Literature allows us to build empathy by stepping into characters' shoes and seeing the world through entirely different perspectives. In a fast-paced digital world dominated by fleeting video clips, the quiet act of reading remains a powerful anchor. It sharpens our minds, expands our vocabularies, and keeps the imagination alive and thriving.",
    
    "Nature operates in a delicate, beautiful balance where every living organism plays a vital role. From the smallest microscopic bacteria in the soil to the massive whales swimming in the deep blue ocean, all creatures are interconnected. Forests act as the planet's lungs, absorbing carbon dioxide and providing clean oxygen, while rivers deliver life-giving water across vast continents. However, human industrial activity has disrupted these natural cycles, causing climate patterns to shift unpredictably. Protecting our environment is no longer just a kind gesture; it is a critical necessity for ensuring the survival of future generations on Earth.",
    
    "Cooking is a beautiful blend of precise science and creative artistic expression. It transforms raw, simple ingredients into delightful culinary experiences that engage all five human senses. A chef acts like a scientist when balancing acidic flavors with fats, or using precise heat to create a perfect golden crust. At the same time, choosing vibrant colors and arranging components on a plate requires the eye of a skilled painter. Beyond the physical nutrition it provides, sharing a homemade meal brings people together, fostering deep conversation and creating lasting memories around the dinner table across every culture.",
    
    "Video games have evolved from simple pixelated blocks into deeply immersive narrative experiences that rival Hollywood cinema. In the early days, players chased high scores on basic arcade screens with limited sound effects. Today, modern gaming offers vast open worlds with stunning photorealistic graphics, complex orchestral scores, and deeply emotional storytelling. Players can explore ancient historical settings, pilot spaceships through distant galaxies, or collaborate with friends globally in real time. This interactive medium empowers users to become active participants in a story, making gaming one of the most powerful and popular forms of entertainment.",
    
    "Resilience is the remarkable ability to bounce back from difficult situations, failures, and unexpected life challenges. Life rarely follows a perfectly straight path, and everyone encounters obstacles that can feel completely overwhelming. True strength does not mean never falling down; rather, it is measured by the willingness to stand up and keep moving forward. Cultivating a resilient mindset requires patience, self-compassion, and a willingness to view failures as valuable learning opportunities. By embracing hardships instead of fearing them, we develop the inner fortitude necessary to navigate the unpredictable twists and turns of our personal journeys.",
    
    "The deep ocean remains one of the least explored and most mysterious frontiers on our planet. While we have mapped the surfaces of the moon and Mars, much of the seabed is shrouded in complete darkness. Deep below the surface, extreme pressure and freezing temperatures create an environment that seems entirely alien to us. Yet, bizarre creatures thrive there, using bioluminescence to glow in the dark and hunt for food. Studying these ocean depths helps scientists understand the origins of life and discovers unique ecosystems that challenge our assumptions about how living organisms survive without any sunlight.",
    
    "Music is a universal language that transcends political borders, cultural barriers, and historical eras. A simple melody has the unique power to evoke deep nostalgia, trigger intense joy, or bring comfort during times of sorrow. Whether it is a grand classical symphony, a rhythmic jazz solo, or an energetic pop anthem, music connects directly with human emotions. Scientists have discovered that listening to music activates multiple areas of the brain, improving memory and reducing stress levels. It accompanies us through life's most important milestones, providing a beautiful soundtrack to our personal memories and shared cultural experiences.",
    
    "For millions of people around the globe, a morning cup of coffee is an essential daily ritual. The rich aroma of freshly roasted beans serves as a comforting wake-up call for the mind. What began centuries ago as a traditional drink in Ethiopia has transformed into a massive global industry and culture. Coffee shops have become modern community hubs where people gather to work, read, or chat with friends. Whether you prefer a strong espresso, a creamy latte, or a cold brew, this caffeinated beverage provides a small moment of warmth and focused energy in a busy world."
]
def typing_test(sentences,paragraph):
    print("The Typing Speed Test is divided into 2 stages. In Stage 1, you will be provided with a set of 5 sentences one by one. In Stage 2, you will be provided with a short paragraph. ALL THE BEST!\n")
    print("\nPress the start button to start the test")
    #here you need to add a button named start, pressing which the execution continues
    print("\nSTAGE-1: SINGLE SENTENCES")
    print("Type the following sentences:")
    time.sleep(2)
    sumt=0
    suma=0
    sumw=0
    for i in range (5):
        sentence = random.choice(sentences)
        sentences.remove(sentence)
        print(f"\n{sentence}")
        start_time = time.time()
        user_input = input()
        end_time = time.time()
        elapsed_time = end_time - start_time
        words = sentence.split()
        word_count = len(words)
        correct_words = sum(1 for w in user_input.split() if w in words)
        accuracy = (correct_words / len(words)) * 100
        sumt+=elapsed_time
        suma+=accuracy
        wpm = (len(user_input.split()) / elapsed_time) * 60
        sumw+=wpm
    stg1time=sumt
    stg1acc=suma/5
    stg1wpm=sumw/5
    time.sleep(3)
    print("\n\nSTAGE-2: PARAGRAPH:")
    print("Type the following paragraph:\n")
    time.sleep(3.5)
    para=random.choice(paragraph)
    print(para+"\n")
    start_time=time.time()
    user_input = input()
    end_time = time.time()
    stg2time = end_time - start_time
    words = para.split()
    word_count = len(words)
    correct_words = sum(1 for w in user_input.split() if w in words)
    stg2acc = (correct_words / len(words)) * 100
    stg2wpm = (len(user_input.split()) / stg2time) * 60
    #displaying the final results
    print("\n\nRESULTS AND ANALYSIS:")
    print("\nSTAGE-1:")
    print(f"Time taken: {stg1time:.2f} seconds")
    print(f"Accuracy: {stg1acc:.2f}%")
    print(f"Typing Speed (words per min): {stg1wpm:.2f}")
    print("\nSTAGE-2:")
    print(f"Time taken: {stg2time:.2f} seconds")
    print(f"Accuracy: {stg2acc:.2f}%")
    print(f"Typing Speed (words per min): {stg2wpm:.2f}")
    print("\nOVERALL:")
    print(f"Total Time taken: {(stg2time+stg1time):.2f} seconds")
    print(f"Mean Accuracy: {((stg1acc+stg2acc)/2):.2f}%")
    print(f"Net Typing Speed (words per min): {((stg1wpm+stg2wpm)/2):.2f}")

typing_test(sentences,paragraphs)