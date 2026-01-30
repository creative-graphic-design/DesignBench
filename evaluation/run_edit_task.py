from dotenv import load_dotenv
from loguru import logger
from tqdm import tqdm

from design_bench.evaluator.compile import collect_compile_information
from design_bench.evaluator.config import Task
from design_bench.evaluator.main import evaluate_edit

load_dotenv()


def main():
    logger.remove()
    logger.add(lambda msg: tqdm.write(msg, end=""))

    models = [
        # "claude-3-7-sonnet-20250219",
        "gpt-4o-2024-11-20",
        # "gemini-2.0-flash",
        # "Llama-3.2-90B-Vision-Instruct",
        # "Llama-3.2-11B-Vision-Instruct",
        # "pixtral-large-latest",
        # "pixtral-12b-2409",
        # "qwen2.5-vl-72b-instruct",
        # "qwen2.5-vl-7b-instruct",
    ]

    frame_works = [
        "react",
        "vue",
        "angular",
        "vanilla",
    ]  # the framework used to actually implement the webpage.
    modes = ["both", "code", "image"]  # code, image, both

    # eval
    evaluate_edit(
        models=models, frame_works=frame_works, modes=modes, llm_judge_flag=False
    )
    evaluate_edit(
        models=models, frame_works=frame_works, modes=modes, llm_judge_flag=True
    )

    # collect the compile information
    for frame_work in frame_works:
        if frame_work == "vanilla":
            continue
        for mode in modes:
            collect_compile_information(
                task_name=Task.EDIT,
                frame_work=frame_work,
                implemented_framework_or_mode=mode,
            )


if __name__ == "__main__":
    main()
