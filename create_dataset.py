import numpy as np 
def get_corpus_to_csv(input_corpus,inference_flag):
    key=5
    o_c=[]
    e_c=[]
    for i in input_corpus:
        o_c.append(ord(i))
        e_c.append(ord(i)+key)
    o_c=np.asarray(o_c).reshape(-1,1)
    if inference_flag==1:
        return o_c
    else: 
        e_c=np.asarray(e_c).reshape(-1,1)
        print('Dataset Prepared')
        print(f'{len(o_c),len(e_c)}')
        np.savez('mydata.npz', origina_txt=o_c, encrypted_txt=e_c)

def convert_numpy_array_to_op_string(numpy_array):
    numpy_lst=list(np.squeeze(numpy_array))
    #print(numpy_lst)
    numpy_lst=[chr(int(round(i))) for i in numpy_lst]
    numpy_lst=''.join(numpy_lst)
    print(f'Decrypted Text: {numpy_lst}')

if __name__=="__main__":
    corpus_text='The world was vast and ever-changing. Check it do you think this shit will work! I mean I am just testing my theory out !!.The sky above was an endless expanse of blue, occasionally interrupted by a passing cloud. The sun shone brightly, casting a warm glow over the land below.I came across a stream, its clear waters rushing over rocks and pebbles. I knelt down at the water\'s edge, cupping my hands and taking a drink. The water was cool and refreshing, and I felt invigorated by its purity.Continuing on my journey, I passed through forests and meadows, across rivers and over hills. I saw creatures of all kinds, from small rodents scurrying about to majestic deer grazing in the fields.As the sun began to set, I found myself atop a hill overlooking a vast expanse of land. The sky was now ablaze with shades of orange and red, a stunning display of nature\'s beauty. In that moment, I felt a deep connection to the world around me, a sense of oneness with all living things.As I descended the hill and made my way back to civilization, I knew that I would never forget the beauty and majesty of the natural world. It was a reminder of the power and wonder of life, and I felt grateful to have experienced it.galaxies, each with billions of stars and countless planets. Our own galaxy, the Milky Way, is just one among many. It is a barred spiral galaxy, with a central bar-shaped structure surrounded by spiral arms. The Sun and its planets lie within one of these arms, known as the Orion Arm. The universe is believed to have begun with the Big Bang, a colossal explosion that occurred roughly 13.8 billion years ago. At the moment of the Big Bang, all matter and energy were contained within a single, infinitely hot and dense point known as a singularity. As the universe rapidly expanded and cooled, matter began to clump together and form stars and galaxies.The study of the universe is known as astronomy, and it encompasses a wide range of disciplines, including astrophysics, cosmology, and planetary science. Astrophysics is the study of the physical properties of celestial objects, including their composition, temperature, and motion. Cosmology is the study of the large-scale structure and evolution of the universe as a whole, including the origins of galaxies and the cosmic microwave background radiation. Planetary science is the study of the planets, moons, and other objects in our solar system and beyond, including their composition, geology, and atmospheres.'
    get_corpus_to_csv(corpus_text,0)
