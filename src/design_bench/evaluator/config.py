from enum import StrEnum, auto
from typing import Dict, Final

DesignBench_Path = ""


class Framework(StrEnum):
    vanilla = auto()
    react = auto()
    vue = auto()
    angular = auto()


class Task(StrEnum):
    repair = auto()
    generation = auto()
    edit = auto()
    compile = auto()


class Mode(StrEnum):
    code = auto()
    image = auto()
    both = auto()
    mark = auto()


key_path = DesignBench_Path + "code/prompting/key.json"

firefox_path = DesignBench_Path + "code/evaluator/geckodriver"

folder_dic: Final[Dict[Task, str]] = {
    Task.generation: DesignBench_Path + "data/generation/",
    Task.edit: DesignBench_Path + "data/edit/",
    Task.repair: DesignBench_Path + "data/repair/",
}

deploy_link_dic: Final[Dict[Framework, str]] = {
    Framework.vue: "http://localhost:5173/",  # npm run dev
    Framework.react: "http://localhost:3000/",  # npm run dev
    Framework.angular: "http://localhost:4200/",  # ng serve
}

project_code_path_dic: Final[Dict[Framework, str]] = {
    Framework.vue: DesignBench_Path + "web/my-vue-app/src/components/HelloWorld.vue",
    Framework.react: DesignBench_Path + "web/my-react-app/app/page.tsx",
    Framework.angular: DesignBench_Path
    + "web/my-angular-app/src/app/new.component.html",
    # "angular": {
    #     "html": DesignBench_Path + "web/my-angular-app/app/new.component.html",
    #     "ts": DesignBench_Path + "web/my-angular-app/app/new.component.ts"
    # }
}

format_dic: Final[Dict[Framework, str]] = {
    Framework.vue: "vue",
    Framework.react: "jsx",
    Framework.value: "html",
    Framework.angular: "angular",
}
