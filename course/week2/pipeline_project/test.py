from src.system import DigitClassifierSystem

system = DigitClassifierSystem.load_from_checkpoint("course/week2/pipeline_project/artifacts/ckpts/train_flow/epoch=5-step=9000.ckpt")

print(system)