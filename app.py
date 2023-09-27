from PIL import Image
from samgeo.fast_sam import SamGeo
import matplotlib
import gradio as gr
matplotlib.use('Agg')
sam = SamGeo(model="FastSAM-x.pt")

def run(img) :
  sam.set_image(img)
  sam.everything_prompt(output="mask.tif")
  result = sam.show_anns("mask.png")
  result = Image.open("mask.png")
  return result

# Define Gradio interface
iface = gr.Interface(
    fn=run,
    inputs=gr.Image(label="Input Image"),
    outputs=gr.Image(label="Output image with predicted instance Masks", type="pil"),
    title="Fast SAM Satellite Imagery Segmentation",
    allow_flagging=False ,
    examples = ["1.png" ,"2.png"] , 
    description="Segment Satellite imagery using Fast Segment Anything Model (SAM).",
)

# Launch the Gradio app
iface.launch(debug=True)
