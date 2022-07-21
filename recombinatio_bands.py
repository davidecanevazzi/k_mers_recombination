from PIL import Image
import ast


def get_concat_h(im1, im2):
    dst = Image.new('RGB', (im1.width + im2.width, im1.height))
    dst.paste(im1, (0, 0))
    dst.paste(im2, (im1.width, 0))
    return dst

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    with open('fat_unique_k_mers_KANSL.txt', 'r') as f:
        tuple=ast.literal_eval(f.read())
        f_uniq=set(tuple[0])
    with open('mot_unique_k_mers_KANSL.txt', 'r') as m:
        m_uniq = ast.literal_eval(m.read())

    f_uniq=set(f_uniq)
    print(type(f_uniq))
    print(type(m_uniq))
    width=1
    height=1000

    img_mom=Image.new(mode="RGB", size=(width,height), color="#FF0000")   # red = mom
    img_dad=Image.new(mode="RGB", size=(width, height), color="#00CC00")  # green = father
    img_not=Image.new(mode="RGB", size=(width,height), color="#000066")

    image = get_concat_h(img_not, img_not)

    with open("9720fb58-7b75-4d7c-a835-cb5e947f3f3c.fasta") as fasta:
        str=fasta.readline()
        for i in range(len(str)-11):
            k_mer=str[i:i+12]
            if k_mer in f_uniq:
                image = get_concat_h(image, img_dad)
            elif k_mer in m_uniq:
                image = get_concat_h(image, img_mom)
            else:
                image = get_concat_h(image, img_not)

    image.show()
    print("done")


