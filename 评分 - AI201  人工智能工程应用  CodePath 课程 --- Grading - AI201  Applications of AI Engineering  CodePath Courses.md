## AI201 | Applications of AI Engineering  
AI201 | 人工智能工程的应用

## Applications of AI Engineering Summer 2026 (@ Section 1A | Tuesday 5PM - 7PM PT)  
2026 年人工智能工程应用夏季课程（@第 1A 组 | 太平洋时间周二下午 5 点至 7 点）

## Personal Member ID#: **115257**  
个人会员编号：115257

Need help? Post on our [class slack channel](http://codepath.slack.com/) or email us at [support@codepath.org](mailto:support@codepath.org)  
需要帮助吗？请在我们的班级 Slack 频道发帖，或发送邮件至 support@codepath.org 与我们联系。

### [](https://courses.codepath.org/courses/ai201/pages/grading#heading-coursework-weighting)Coursework Weighting  课程成绩的权重分配

This table specifies the amount of points a given project of the course has on the final grade.  
此表格指定了课程中某个项目的最终成绩所占的分数。

| Assignment  任务 | Required  必需 | (+Stretch)  (+拉伸) |
| --- | --- | --- |
| Project 1: The Unofficial Guide  
项目 1：非官方指南 | 25 | (+5) |
| Project 2: FitFindr  项目 2：FitFindr | 25 | (+7) |
| Project 3: TakeMeter  项目 3：TakeMeter | 25 | (+4) |
| Project 4: Provenance Guard  
项目 4：来源追溯系统 | 25 | (+4) |
| Project 5: Mixtape Bug Hunt  
项目 5：混音带寻宝游戏 | 25 | (+3) |
| Project 6: CineLog  项目 6：CineLog 格式 | 25 | (+3) |
| Week 7: Issue Selection  
第 7 周：议题选择 | 10 | — |
| Week 8: Reproduction and Planning  
第 8 周：繁殖与规划 | 10 | — |
| Week 9: PR Submission  
第 9 周：公关材料提交 | 20 | — |
| Week 10: Reflection  第 10 周：反思 | 10 | — |
| 
**Total  总计**

 | **200** | **(+26)** |

### [](https://courses.codepath.org/courses/ai201/pages/grading#heading-points-and-percentages)Points and Percentages  得分和百分比

**Earned points:** Points a student earns on a given app assignment based on the completion of required features.  
获得分数：学生在给定应用程序作业中根据完成所需功能而获得的分数。

**Required points:** The number of points required to earn 100% of the points for a given lab or assignment (i.e. 10 earned pts / 10 total pts = 100% pts for that project).  
所需分数：获得某个实验或作业 100%分数所需分数的数量（例如：10 获得分 / 10 总分 = 该项目的 100%分数）。

**Percentage score:** The overall percentage score for a project equates to the _Earned points_ / _Required points_ for a given project, for example...  
百分比得分：一个项目的总体百分比得分等于已得分 / 所需得分，例如...

-   8 earned points / 10 required points = 80%  
    8 已得分 / 10 所需得分 = 80%
-   10 earned points / 10 required points = 100%  
    10 已得分 / 10 所需得分 = 100%
-   12 earned points / 10 required points = 120%  
    12 已得分 / 10 所需得分 = 120%

### [](https://courses.codepath.org/courses/ai201/pages/grading#heading-project-features)Project Features  项目特性

-   Completion of **ALL required features** for a given assignment will earn 100% of the points for that assignment. If all required features are **NOT** completed, a grade will be assigned proportional to the point values for any completed features.  
    完成指定任务的所有必需特性将获得该任务 100%的分数。如果所有必需特性未完成，则成绩将根据已完成特性的分值按比例分配。
-   Completion of **stretch features** will earn additional points that may allow the student's percentage score to exceed 100%.  
    完成扩展特性将获得额外的分数，这可能使学生的百分比得分超过 100%。

## [](https://courses.codepath.org/courses/ai201/pages/grading#heading-project-grading)Project Grading  项目评分

### [](https://courses.codepath.org/courses/ai201/pages/grading#heading-project-1-the-unofficial-guide)Project 1: The Unofficial Guide  
项目 1：非官方指南

Total Points: **25pts** + 5pts bonus  
总积分：25 分 + 5 分奖励分

Required Features  所需功能

| **3pts  3 分** | **Document Pipeline — Ingestion and Chunking  
文档处理流程——数据摄取与分块处理** |
| --- | --- |
| 1 | README names the domain and identifies at least 10 documents with specific sources (URLs, subreddit names, or file descriptions).  
README 文件中列出了该域名的相关信息，并指明了至少 10 份具有明确来源的文档（包括 URL 地址、子版块名称或文件描述）。 |
| 1 | Chunking strategy is explained with specific reasoning — chunk size, overlap, and why those numbers fit the structure of the documents.  
关于“分块策略”的解释包含了具体的理由——即分块的规模、各分块之间的重叠程度，以及为什么这些数值能够符合文档的结构特点。 |
| 1 | README includes at least 5 labeled sample chunks with their source document name.  
README 文件中至少包含 5 个带有标签的示例代码片段，同时还会注明这些代码片段的来源文档名称。 |

| **4pts  4 分** | **Retrieval — Relevant Chunks Returned for Queries  
检索——根据查询条件返回的相关内容/片段** |
| --- | --- |
| 1 | README includes at least 3 retrieval test examples, each showing the query and the top returned chunks.  
README 文件中至少包含 3 个检索测试示例，每个示例都展示了查询内容以及检索结果中的前几条记录。 |
| 1 | For at least 2 of those examples, the student provides a written explanation of why the returned chunks are relevant to the query.  
在其中的至少两个例子中，学生都给出了书面解释，说明为什么返回的那些内容与查询需求相关。 |
| 1 | README names the embedding model used.  
README 文件中说明了所使用的嵌入模型。 |
| 1 | README includes a tradeoff reflection — what factors the student would weigh when choosing a model for a production deployment (e.g., cost, context length, multilingual support, local vs. API latency).  
README 中还探讨了各种权衡因素——学生在选择用于实际部署的模型时，会考虑哪些因素呢？比如成本、上下文长度、多语言支持能力，以及本地处理与通过 API 调用时的延迟情况。 |

| **3pts  3 分** | **Grounded Generation with Source Attribution  
具有来源归属功能的“ grounded generation”技术** |
| --- | --- |
| 1 | README includes at least 2 example system responses with source attribution visible in the output text.  
README 文件中至少包含 2 个系统响应的示例，且这些示例的源代码信息在输出文本中清晰可见。 |
| 1 | README includes one out-of-scope query example with the system's refusal response shown.  
README 文件中包含了一个超出系统处理范围的查询示例，同时展示了系统对此的拒绝响应。 |
| 1 | README explains how grounding is enforced in the prompt or pipeline.  
README 文档说明了如何在提示词或处理流程中实现“接地”机制。 |

| **4pts  4 分** | **Evaluation Report  评估报告** |
| --- | --- |
| 1 | All 5 test questions are documented, each with the question, the expected correct answer, and the system's actual response.  
所有 5 道测试题都有详细的记录，包括每道题的题目、正确答案以及系统的实际回答。 |
| 1 | An accuracy judgment is given for each question (accurate / partially accurate / inaccurate).  
每道题都会被给出一个准确度判断：准确/部分准确/不准确。 |
| 2 | At least one failure case is identified with a specific cause tied to a part of the pipeline — not just "it got it wrong," but why (e.g., "the relevant sentence was split across a chunk boundary").  
至少有一个故障案例被明确指出其具体原因，这些原因都与管道的某个特定部分有关——不仅仅是“出了错”，而是具体出错的原因是什么（例如：“相关句子被分到了不同的数据块中”）。 |

| **2pts  2 分** | **Query Interface  查询接口** |
| --- | --- |
| 2 | README describes the interface's input and output fields and includes a sample interaction transcript showing a complete query and response.  
README 文档介绍了该界面的输入和输出字段，同时还包含了一个示例交互记录，展示了完整的查询过程和响应结果。 |

| **4pts  4 分** | **`planning.md` Completeness   `planning.md` 完整性** |
| --- | --- |
| 1 | Domain — names the domain and explains why this knowledge is valuable or hard to find through official channels.  
域名——说明该域名的具体含义，并解释为何了解该域名具有价值，或者为何无法通过官方渠道获取这些信息。 |
| 1 | Documents — lists specific sources with enough detail to locate them; Chunking Strategy — states chunk size, overlap, and explains fit for the document type; Retrieval Approach — names the embedding model, states top-k value, and includes a tradeoff reflection on production model selection. All three sub-sections must be present and substantive.  
文档相关内容——列出具体的信息来源，并提供足够的详细信息以便于定位这些来源；分块策略——明确说明每个数据块的规模、各数据块之间的重叠程度，以及该策略如何适用于不同类型的文档；检索方式——说明所使用的嵌入模型、top-k 值的相关信息，同时还会对生产环境中的模型选择进行必要的权衡分析。这三个子部分都是不可或缺的，且必须包含足够详细的信息。 |
| 1 | Evaluation Plan — lists all 5 test questions with specific, verifiable expected answers (not open-ended).  
评估计划——列出了全部 5 道测试题，每道题都配有具体且可验证的预期答案（非开放式问题）。 |
| 1 | Anticipated Challenges — names at least 2 specific risks with reasoning; AI Tool Plan — names at least one pipeline component the student planned to use AI to implement.  
预期的挑战——至少列出 2 个具体风险，并说明原因；AI 工具计划——至少说明一个学生计划使用 AI 来实现的流程环节。 |

| **3pts  3 分** | **README Completeness  README 文件的完整性/README 内容的完备性** |
| --- | --- |
| 1 | Domain and document sources; chunking strategy with reasoning; embedding model with tradeoff reflection; how grounded generation is enforced.  
领域与文档来源；基于推理的文本分割策略；具有权衡机制的嵌入模型；如何确保生成的文本内容具有现实依据。 |
| 1 | Full evaluation report (all 5 questions with expected answers, system responses, and accuracy judgments).  
完整的评估报告（包括全部 5 个问题：预期答案、系统给出的回答以及准确度评估）。 |
| 1 | At least one honest failure case with a specific cause; spec reflection (one way the spec helped, one divergence and why).  
至少要有一个有明确原因的、属于“诚实失败”的案例；同时需要对该需求进行反思：该需求起到了什么作用、存在哪些偏差，以及原因何在。 |

| **2pts  2 分** | **AI Usage Transparency  人工智能使用的透明度** |
| --- | --- |
| 1 | Section describes at least 2 specific instances of AI tool use, naming what the student directed the AI to do in each case.  
该部分需至少列举两个使用人工智能工具的实例，并详细说明在每个案例中，学生具体指示人工智能执行了什么任务。 |
| 1 | Each instance describes what the student reviewed, revised, or overrode. The section reads as genuine collaboration — the student was directing, not just accepting output.  
每个记录都详细说明了学生具体审查、修改或否决了哪些内容。从这些记录来看，这显然是一种真正的协作过程——学生并非只是被动地接受结果，而是主动参与其中的决策过程。 |

Stretch Features  拉伸功能

| **+2pts  +2 分** | **Hybrid Search  混合搜索** |
| --- | --- |
|  | README describes the hybrid approach (how BM25 and semantic scores are combined) and reports a comparison on at least 3 queries — what each method returned and which performed better.  
README 文档详细介绍了这种混合式处理方法（即如何将 BM25 算法与语义评分相结合），并针对至少 3 个查询进行了对比测试：分别说明了每种方法的结果，以及哪种方法的性能更佳。 |
|  | Demo or source shows hybrid search in operation.  
演示或源代码展示了混合搜索的运作过程。 |

| **+1pt  +1 分** | **Chunking Strategy Comparison  
分块策略比较** |
| --- | --- |
|  | README reports comparison results across 2+ chunking strategies on the same query set. Analysis states which strategy performed better and explains why, with reference to specific query results.  
README 文件展示了针对同一查询集，两种及以上分块策略的比较结果。分析部分指出了哪种策略表现更好，并结合具体的查询结果说明了原因。 |

| **+1pt  +1 分** | **Metadata Filtering  元数据过滤** |
| --- | --- |
|  | Demo or source shows a query being filtered by at least one metadata field (source, date, or rating) with a visible effect on which results are returned.  
演示或源代码显示：查询结果是通过至少一个元数据字段（如来源、日期或评分）来过滤的，这一过滤过程会直接影响最终返回的结果。 |

| **+1pt  +1 分** | **Conversational Memory  对话记忆** |
| --- | --- |
|  | Demo or source shows a multi-turn exchange where the second query references context from the first, and the response reflects that memory — not just a coincidence of topic overlap.  
演示或源代码显示了多轮对话的情景：在第二次提问时，会引用第一次提问中的上下文信息，而回答则体现了对这一上下文的记忆——这并非仅仅是话题上的巧合而已。 |

***

### [](https://courses.codepath.org/courses/ai201/pages/grading#heading-project-2-fitfindr)Project 2: FitFindr  项目 2：FitFindr

Total Points: **25pts** + 7pts bonus  
总积分：25 分 + 7 分奖励分

Required Features  所需功能

| **4pts  4 分** | **Three Tools with Defined Interfaces  
三种具有明确接口的工具** |
| --- | --- |
| 1 | README lists all 3 required tools, each with a named function.  
README 文件列出了所有 3 个必需的工具，每个工具都配有相应的功能说明。 |
| 1 | Each tool's inputs are described with parameter names and types (e.g., "`description` (str), `size` (str), `max_price` (float)").  
每个工具的输入参数都用参数名称和类型来表示（例如：“ `description` (str), `size` (str), `max_price` (float)”）。 |
| 1 | Each tool's return value is described — not just "returns a list," but what's in the list.  
每种工具的返回值都有详细的说明——不仅仅是“返回一个列表”，还说明了列表中包含的内容。 |
| 1 | Demo or source shows all 3 tools being called within a single interaction.  
演示或源代码显示：在单次操作中，这三个工具都被调用了。 |

| **2pts  2 分** | **Multi-Step Workflow End to End  
多步骤工作流程的端到端处理** |
| --- | --- |
| 1 | Demo or source shows a complete interaction that starts with a natural language user query and ends with a fit card, using all 3 required tools along the way.  
该演示或源代码展示了完整的交互过程：从用户用自然语言提出的查询开始，到最终生成相应的推荐结果为止。在整个过程中，所有三个必需的工具都被妥善使用了。 |
| 1 | The demo narration or the README / `planning.md` walkthrough explains what the agent is doing at each step — which tool is being called and why.  
演示说明或 README 文件/操作指南会详细解释该智能体在每个步骤中具体在做什么——究竟调用了哪个工具，以及为何要调用该工具。 |

| **3pts  3 分** | **State Management Across Tool Calls  
跨工具调用的状态管理** |
| --- | --- |
| 1 | Demo or source shows that the item returned by `search_listings` is the same item passed into `suggest_outfit` — without the user re-entering it.  
演示或源代码显示， `search_listings` 返回的参数与传递给 `suggest_outfit` 的参数完全相同——用户无需重新输入这些参数。 |
| 1 | Demo or source shows the outfit from `suggest_outfit` passing into `create_fit_card` without re-entry.  
演示或源代码显示：来自 `suggest_outfit` 的物品可以直接传递给 `create_fit_card` ，而无需再次输入。 |
| 1 | README describes the state management approach: what is stored, when, and how it passes between tools.  
README 文档详细介绍了状态管理的方式：究竟存储了什么内容、在何时存储、以及这些数据是如何在各个工具之间传递的。 |

| **4pts  4 分** | **Planning Loop Adaptiveness  
规划循环的适应性** |
| --- | --- |
| 1 | README explains the planning loop's conditional logic — what state it checks and what triggers each decision. "It decides what to do next" does not earn this point.  
README 文档详细解释了规划循环中的条件逻辑——即系统会检查哪些状态，以及是什么因素触发了各个决策。“决定下一步该做什么”这一表述并不足以准确描述这一过程。 |
| 1 | README describes what the agent does specifically when `search_listings` returns no results (not just "it handles errors").  
README 文件详细说明了当 `search_listings` 没有返回任何结果时，该代理具体会执行什么操作（而不仅仅是“处理错误”）。 |
| 2 | Demo or source shows the agent behaving differently for a non-standard input compared to the happy path — the agent doesn't call all tools unconditionally in the same sequence.  
在演示或源代码中可以发现：对于非标准输入，该智能体的行为与“正常情况”下有所不同——它不会无条件地按照相同的顺序调用所有工具。 |

| **3pts  3 分** | **Error Handling  错误处理** |
| --- | --- |
| 1 | README describes the specific failure mode for each of the 3 required tools and what the agent does in each case.  
README 文档详细说明了这 3 个必备工具各自的故障模式，以及代理程序在各种情况下的具体处理方式。 |
| 1 | Demo or source shows handling for at least one deliberately triggered failure (not a happy-path edge case — an actual failure).  
演示或源代码应能够展示如何处理至少一次人为引发的故障情况（并非那种正常的、理想的测试场景，而是真正的故障情况）。 |
| 1 | Demo or source shows the agent's response to the failure is specific and actionable — it tells the user what failed and what to try next.  
演示或源代码表明，该代理对故障的反应是具体且可行的——它会告诉用户到底哪里出了问题，以及接下来应该采取什么措施。 |

| **4pts  4 分** | **`planning.md` Quality   `planning.md` 质量** |
| --- | --- |
| 1 | Tools — all 3 required tools described with name, inputs (name + type), return value, and what the agent does on failure.  
工具——列出了所有 3 种必需的工具，包括工具的名称、输入参数的名称和类型、返回值，以及当工具无法正常工作时，代理应采取的措施。 |
| 1 | Planning Loop — conditional logic described (not just intent); State Management — what is stored and how it flows.  
规划循环——即所描述的条件逻辑（而不仅仅是意图本身）；状态管理——指的是存储了什么以及这些状态是如何被处理的。 |
| 1 | Error Handling table — completed with specific agent responses for each tool's failure mode; Complete Interaction walkthrough — traces the example query step-by-step through all three tool calls.  
错误处理表格——详细列出了每种工具在出现故障时的具体处理方式；完整的交互流程演示——逐步展示了该查询在经过三种工具处理后的全过程。 |
| 1 | Architecture diagram — shows data and control flow through the agent; AI Tool Plan — names specific spec sections used to prompt AI tools and describes how generated code was verified against the spec.  
架构图——展示了数据在各个组件之间的流动方式以及控制流程；AI 工具计划——列出了用于向 AI 工具提供指令的具体规范内容，并说明了如何根据这些规范来验证生成的代码。 |

| **3pts  3 分** | **README Completeness  README 文件的完整性/README 内容的完备性** |
| --- | --- |
| 1 | Tool inventory with inputs, outputs, and purpose for each tool; planning loop explanation with conditional logic; state management approach.  
包含每种工具的输入、输出及用途的工具清单；包含条件逻辑的规划流程说明；状态管理方法。 |
| 1 | Error handling per tool with at least one concrete example from testing.  
每种工具的错误处理方式都应至少有一个来自测试的实际例子来加以说明。 |
| 1 | Spec reflection (one way the spec helped, one divergence and why).  
规格的反映作用（规格带来的积极影响、存在的差异以及原因）。 |

| **2pts  2 分** | **AI Usage Transparency  人工智能使用的透明度** |
| --- | --- |
| 1 | Section describes at least 2 specific instances of AI tool use, naming what the student directed the AI to do in each case.  
该部分需至少列举两个使用人工智能工具的实例，并详细说明在每个案例中，学生具体指示人工智能执行了什么任务。 |
| 1 | Each instance describes what the student reviewed, revised, or overrode.  
每条记录都详细说明了学生已经审阅、修改或否决了哪些内容。 |

Stretch Features  拉伸功能

| **+2pts  +2 分** | **Price Comparison Tool  价格比较工具** |
| --- | --- |
|  | Demo or source shows the tool returning a price assessment with reasoning based on comparable listings in the dataset. README describes how comparisons are made.  
演示版或源代码显示，该工具会根据数据集中的同类房源信息来给出价格评估结果，并附有相应的推理过程。README 文件则详细说明了比较的具体方式。 |

| **+2pts  +2 分** | **Style Profile Memory  风格档案记忆** |
| --- | --- |
|  | Demo or source shows two interactions where the second uses style preferences from the first without re-entry. README describes the storage approach.  
演示版或源代码展示了两种交互方式：第二种方式直接使用了第一种方式中设定的样式偏好，而无需再次输入。README 文档则详细说明了数据存储的方式。 |

| **+2pts  +2 分** | **Trend Awareness Tool  趋势感知工具** |
| --- | --- |
|  | Demo or source shows the tool returning trend information that visibly influences the outfit suggestion. README describes the data source used.  
演示版或源代码显示，该工具会返回影响服装推荐结果的趋势信息。README 文件则介绍了所使用的数据来源。 |

| **+1pt  +1 分** | **Retry Logic with Fallback  
带有回退机制的重试逻辑** |
| --- | --- |
|  | Demo or source shows the agent handling a zero-result search by automatically retrying with loosened constraints, explaining to the user what was adjusted.  
演示或源代码展示了该智能体如何处理搜索无结果的情况：它会自动调整搜索条件后重新尝试搜索，并向用户说明所做的调整内容。 |

***

### [](https://courses.codepath.org/courses/ai201/pages/grading#heading-project-3-takemeter)Project 3: TakeMeter  项目 3：TakeMeter

Total Points: **25pts** + 4pts bonus  
总积分：25 分 + 4 分奖励分

Required Features  所需功能

| **3pts  3 分** | **Label Taxonomy  标签分类法** |
| --- | --- |
| 1 | 2–4 labels are defined in complete sentences with clear boundaries between them.  
2 到 4 个标签都是用完整的句子来描述的，各个标签之间有明确的界限。 |
| 1 | Each label has 2 example posts included.  
每个标签下都包含 2 篇示例帖子。 |
| 1 | Definitions are specific enough that two people reading them would likely agree on most cases — not one-word descriptions or vague adjectives.  
这些定义足够具体，因此，只要两个人阅读了这些定义，那么在大多数情况下，他们应该会达成一致——而不是那种只用一个词来描述或使用含糊不清的形容词的描述方式。 |

| **4pts  4 分** | **Annotated Dataset  带注释的数据集** |
| --- | --- |
| 1 | Dataset has at least 200 labeled examples.  
该数据集至少包含 200 个带有标签的样本。 |
| 1 | README documents the data source, labeling process, and label distribution (count per label).  
README 文档详细介绍了数据来源、标注流程以及各标签的分布情况（即每个标签出现的次数）。 |
| 1 | At least 3 genuinely difficult examples are described, including the labeling decision made for each.  
文中至少列举了 3 个真正具有挑战性的例子，并对每个例子中的标注决策进行了详细说明。 |
| 1 | No single label accounts for more than 70% of the dataset.  
没有任何一个标签在数据集中所占的比例超过 70%。 |

| **2pts  2 分** | **Fine-Tuning Pipeline  微调流程/精细调整步骤** |
| --- | --- |
| 1 | README names the base model and the training platform (e.g., Colab, local, HuggingFace AutoTrain).  
README 文件中列出了基础模型以及训练平台的信息（例如：Colab、本地环境、HuggingFace AutoTrain）。 |
| 1 | At least one key training decision is described and justified — e.g., number of epochs, learning rate, or batch size, with reasoning or observation (not just "I used the default").  
至少需要说明并解释一项关键的训练参数选择——比如训练周期的数量、学习率或批量大小等。解释时需要给出合理的依据或观察结果，而不能只是简单地说“我使用了默认值”。 |

| **2pts  2 分** | **Baseline Comparison  基线对比** |
| --- | --- |
| 1 | README describes the baseline approach — the prompt used and how results were collected.  
README 文件介绍了基准测试的方法——即所使用的提示语以及结果收集的方式。 |
| 1 | Evaluation report shows performance metrics for both the fine-tuned model and the baseline on the same test set.  
评估报告展示了在相同测试集上，经过微调的模型与基准模型的各项性能指标。 |

| **5pts  5 分** | **Evaluation Report and Error Analysis  
评估报告与错误分析** |
| --- | --- |
| 1 | At least one per-class metric is reported for the fine-tuned model (precision, recall, or F1 — not just overall accuracy).  
对于经过微调的模型，至少会报告一项每类的评估指标（精确度、召回率或 F1 值——而不仅仅是整体准确率）。 |
| 1 | A confusion matrix or equivalent table is included showing where the model confuses labels.  
该报告还包含了一个混淆矩阵或类似的表格，用于显示模型在哪些情况下将不同的标签搞混了。 |
| 1 | At least 3 specific wrong predictions are analyzed — each with an explanation tied to the data, the label boundary, or the model's behavior (not just "it got it wrong").  
至少分析了 3 个具体的错误预测——对于每一个错误预测，都给出了与数据、标签边界或模型行为相关的解释（而不仅仅是简单地说“预测错了”）。 |
| 2 | A reflection on the gap between what the model captured and what was intended — describes a specific failure pattern (a label pair, a post type, a distributional issue) rather than a generic observation like "it needs more data."  
对模型所捕捉到的结果与实际预期之间的差距的反思——这种描述指的是某种具体的故障模式（比如某个标签对、某种帖子类型、某种分布问题），而不是像“需要更多数据”这样的笼统说法。 |

| **4pts  4 分** | **`planning.md`** |
| --- | --- |
| 1 | Community choice is explained — not just named, but with reasoning for why it's a good fit for this task.  
文中详细解释了“社区选择”这一概念——不仅说明了其名称的由来，还阐述了为何它是最适合解决这项任务的方案。 |
| 1 | Labels are defined with examples and the hardest anticipated edge case is named and addressed.  
这些标签都通过具体示例来加以说明，同时，那些最有可能出现的复杂情况也都被明确指出并得到了妥善处理。 |
| 1 | Data collection plan and evaluation metrics are described, with reasoning for the chosen metrics.  
文中详细阐述了数据收集方案和评估指标，并对所选指标的合理性进行了说明。 |
| 1 | A specific definition of "good enough" performance is stated (a concrete threshold, not just "it should work well"); AI Tool Plan covers at least one intended use: label stress-testing, annotation assistance, or failure pattern analysis.  
对“足够好”的性能标准有明确的定义（即有一个具体的阈值，而不仅仅是“能够正常使用”）；该人工智能工具至少能满足以下一种用途：压力测试、注释辅助或故障模式分析。 |

| **3pts  3 分** | **Demo Video  演示视频** |
| --- | --- |
| 1 | Demo or source shows 3–5 posts being classified by the fine-tuned model with label and confidence visible; one correct prediction is narrated/explained with reasoning for why it was correct.  
演示或源代码显示：经过微调的模型能够对 3 到 5 篇帖子进行分类，同时会显示相应的标签和置信度数值。对于每一个正确的预测结果，都会详细说明其正确的原因。 |
| 1 | Demo or source shows one incorrect prediction with an explanation of what went wrong and why — not just "it got it wrong."  
演示或源代码会展示一个错误的预测结果，并详细解释出错的原因——而不仅仅是简单地说“预测错了”。 |
| 1 | README includes an evaluation report summary surfacing the key metrics.  
README 文件中包含了评估报告的摘要，其中列出了各项关键指标。 |

| **2pts  2 分** | **AI Usage and Spec Reflection  
AI 的使用情况与技术规格分析** |
| --- | --- |
| 1 | Section describes at least 2 specific instances of AI tool use: what the student directed the AI to do, and what they revised or overrode. Any AI assistance used during annotation is disclosed (e.g., using an LLM to pre-label examples that were then reviewed and corrected).  
该部分需至少列举两个使用人工智能工具的具体案例：学生让人工智能执行了哪些任务，以及他们对人工智能的决策进行了哪些修改或否定。在注释过程中所使用的一切人工智能辅助工具都应被明确说明出来（例如，使用大型语言模型对样本进行预标记，然后再由人工进行审核和修正）。 |
| 1 | Spec reflection is present and substantive — describes one way the spec helped guide the work and one way implementation diverged from it and why.  
规范层面的反思是真实且重要的——它说明了规范在指导工作过程中所起的作用，同时也说明了实际实施过程中与规范的偏差及其原因。 |

Stretch Features  拉伸功能

| **+1pt  +1 分** | **Inter-Annotator Reliability  
不同注释者之间的可靠性/不同注释者给出的结果的一致性** |
| --- | --- |
|  | README reports agreement rate (Cohen's kappa or percentage agreement) for 30+ examples labeled independently by two people, and disagreements are analyzed.  
该文档报告了由两人独立标记的 30 多个样本的匹配率（科恩卡帕系数或百分比匹配率），同时还将那些存在分歧的样本进行了分析。 |

| **+1pt  +1 分** | **Confidence Calibration  信心校准** |
| --- | --- |
|  | README shows or describes a calibration analysis — do higher confidence predictions correspond to higher accuracy?  
README 文件介绍了校准分析的相关内容——那些置信度较高的预测结果，其准确性是否也更高呢？ |

| **+1pt  +1 分** | **Error Pattern Analysis  错误模式分析** |
| --- | --- |
|  | README identifies a systematic pattern across errors — a generalizable observation about a post type or label pair the model consistently struggles with, with supporting evidence from the error set.  
README 文件揭示了各种错误背后的共同规律——即模型在处理某种帖子类型或标签组合时始终存在困难。这些规律都有相应的错误数据作为佐证。 |

| **+1pt  +1 分** | **Deployed Interface  已部署的接口** |
| --- | --- |
|  | Demo or source shows a working interface that accepts a new post as input and displays the predicted label and confidence score.  
演示版或源代码展示了该系统的实际运行界面：该界面可以接收新的输入内容，然后显示预测出的标签以及置信度得分。 |

***

### [](https://courses.codepath.org/courses/ai201/pages/grading#heading-project-4-provenance-guard)Project 4: Provenance Guard  
项目 4：来源追溯系统

Total Points: **25pts** + 4pts bonus  
总积分：25 分 + 4 分奖励分

Required Features  所需功能

| **3pts  3 分** | **Content Submission Endpoint  
内容提交端点** |
| --- | --- |
| 1 | Demo or source shows a text submission to the API returning a structured JSON response.  
演示或源代码显示了向 API 提交文本后，API 会返回结构化的 JSON 响应。 |
| 1 | The response includes an attribution result and a confidence score.  
该响应包含一个归属结果以及一个置信度得分。 |
| 1 | The response includes transparency label text (not just a raw score).  
该反馈包含详细的说明文字（而不仅仅是原始分数）。 |

| **2pts  2 分** | **Multi-Signal Detection Pipeline  
多信号检测流程** |
| --- | --- |
| 1 | README names 2 or more detection signals and explains what each one captures — not just what tool was used, but what property of the text it measures, and what each signal misses.  
README 文件会列出两种或更多的检测信号，并详细说明每种信号的作用——不仅包括使用了哪种工具，还说明了该工具所测量的文本特征是什么，以及每种信号无法检测到什么内容。 |
| 1 | Demo or source shows results that reference or visibly reflect both signals (e.g., individual signal scores shown alongside the combined score).  
演示或源代码所展示的结果，应能够体现或清晰反映这两个信号的情况（例如，应同时显示各个信号的得分以及综合得分）。 |

| **2pts  2 分** | **Confidence Scoring with Uncertainty  
具有不确定性的置信度评分** |
| --- | --- |
| 1 | Demo or source shows at least two submissions with noticeably different confidence scores — a high-confidence case and a lower-confidence case.  
演示或源代码中应至少包含两个置信度明显不同的样本——一个置信度较高的样本，另一个置信度较低的样本。 |
| 1 | README explains how signals are combined into a confidence score and includes some description of how the student validated that scores are meaningful (e.g., tested inputs that should produce different scores, or described the thresholds separating label categories).  
README 文件详细说明了如何将各种信号组合起来以得出置信度得分。同时，该文件还介绍了学生是如何验证这些得分是否具有实际意义的：例如，他们测试了那些应该产生不同得分的输入数据，还明确了用于区分不同标签类别的阈值。 |

| **3pts  3 分** | **Transparency Label  透明度标签** |
| --- | --- |
| 1 | README includes a mockup of the transparency label — a screenshot or a text/markdown mockup showing the actual label text as a user would see it.  
README 文件中包含了透明度标签的样例——也就是一张截图，或是用文本/Markdown 格式呈现的样例，用以展示用户实际会看到的标签内容。 |
| 1 | The label uses plain language — no jargon like "classifier output" or "logit score." A non-technical reader could understand what it means.  
该标签使用了通俗易懂的语言——没有“分类器输出”或“逻辑斯蒂得分”之类的专业术语。即使是不懂技术的读者也能理解其含义。 |
| 1 | The label visibly differs between high-confidence and low-confidence results — different text, not just a different number.  
高置信度和低置信度的结果在标签上有明显区别——不仅仅是数字不同，文本内容也完全不同。 |

| **2pts  2 分** | **Appeals Workflow  上诉处理流程** |
| --- | --- |
| 1 | Demo or source shows an appeal being submitted with creator reasoning included.  
演示或源代码展示了提交的上诉内容，其中还包括了创建者所阐述的理由。 |
| 1 | Demo or source shows the content's status updated to "under review" and the appeal visible in the audit log.  
演示或源代码显示，该内容的状态已更新为“正在审核中”，而相关的申诉信息也记录在审计日志中。 |

| **2pts  2 分** | **Rate Limiting  速率限制** |
| --- | --- |
| 1 | Demo or source shows rate limiting in action — what happens when the limit is hit (e.g., a 429 response or an error message).  
演示或源代码展示了速率限制的实际效果——当达到限制时会发生什么（例如，返回 429 错误码或显示错误消息）。 |
| 1 | README documents the specific limits chosen and provides reasoning tied to realistic usage patterns on a writing platform — not just "I used the default."  
README 文档详细说明了所选定的各种限制条件，并基于写作平台上的实际使用情况来解释这些限制的合理性——而不仅仅是“我使用了默认设置”这种简单的解释。 |

| **3pts  3 分** | **Audit Log  审计日志** |
| --- | --- |
| 1 | Demo or source shows the audit log with at least 3 entries; each entry visibly includes the attribution result, confidence score, and timestamp.  
演示版或源代码中应包含至少 3 条审计记录；每条记录都应明确显示归属结果、置信度得分以及时间戳。 |
| 1 | Log format is structured — JSON, a table, or a formatted log file. Unformatted console output does not qualify.  
日志格式是结构化的——可以是 JSON 格式、表格形式或格式化的日志文件。未经格式化的控制台输出则不符合要求。 |
| 1 | At least one appeal is visible in the log, showing the appeal alongside the original classification entry.  
在日志中至少可以看到一次上诉记录，该记录与最初的分类信息一起被显示出来。 |

| **4pts  4 分** | **`planning.md`** |
| --- | --- |
| 1 | Detection signals are described with explanation of what each measures and how their outputs are combined.  
对各种检测信号进行了说明，包括每种信号所测量的物理量，以及这些信号的输出数据是如何被组合起来的。 |
| 1 | Uncertainty representation is addressed — specific thresholds or score ranges are defined, not just "it will show a score."  
对不确定性的处理方式也得到了明确——规定了具体的阈值或分数范围，而不仅仅是“会显示出一个分数而已”。 |
| 1 | Transparency label variants are written out for at least the high-confidence AI, uncertain, and high-confidence human cases.  
对于那些被人工智能认定为“高置信度”的案例、那些结果不确定的案例，以及那些被人类认定为“高置信度”的案例，都会详细标注出相关的透明度信息。 |
| 1 | Appeals workflow and at least two anticipated edge cases are described with enough specificity to be useful pre-work; an `## AI Tool Plan` section identifies at least one milestone where AI tools will be used for code generation, specifying what spec sections and diagram will be provided as input.  
该文档详细阐述了相应的处理流程以及至少两种可能的特殊情况，这些信息对于后续的工作具有很高的参考价值。在 `## AI Tool Plan` 部分中，明确指出了至少一个需要使用人工智能工具来生成代码的节点，同时还说明了需要作为输入的各个技术规格和图表。 |

| **2pts  2 分** | **README** |
| --- | --- |
| 1 | Known limitations section names at least one specific content type the system would likely misclassify, with explanation tied to the signals — not a generic disclaimer.  
“已知限制”部分应至少列出一种系统可能误分类的具体内容类型，并对造成误分类的原因进行说明——而不是简单的免责声明。 |
| 1 | Spec reflection is present and substantive — describes a real way implementation diverged from the plan and why.  
具体差异是真实存在的，而且很重要——这些差异说明了实际实施情况与计划之间的偏差，以及产生这种偏差的原因。 |

| **2pts  2 分** | **AI Usage  人工智能的应用场景** |
| --- | --- |
| 1 | Section describes at least 2 specific instances of AI tool use: what the student directed the AI to do and what the output was.  
该部分需至少列举两个具体的 AI 工具使用案例：学生让 AI 执行了什么任务，以及 AI 的输出结果是什么。 |
| 1 | Each instance includes what the student revised, overrode, or decided differently — not just "I used AI to write this function."  
每个实例都包含了学生所做过的修改、所推翻的内容，或是他们自己做出的不同决定——而不仅仅是“我使用人工智能来编写了这个函数”这样的简单描述。 |

Stretch Features  拉伸功能

| **+1pt  +1 分** | **Ensemble Detection  联合检测** |
| --- | --- |
|  | README describes 3 or more distinct detection signals with a documented weighting or voting strategy explaining how conflicts between signals are resolved. Demo or source shows individual signal scores alongside the ensemble result.  
README 文档中详细描述了三种或更多种不同的检测信号，并说明了相应的权重分配或投票机制，从而解释了如何处理这些信号之间的冲突。演示或源代码则展示了各个信号的得分情况以及综合处理后的结果。 |

| **+1pt  +1 分** | **Provenance Certificate  来源证明书** |
| --- | --- |
|  | README describes the certificate design and what verification step a creator completes to earn it. Demo or source shows a verified label appearing on content and distinguishable from the standard transparency label.  
README 文件详细介绍了该证书的设计方式，以及颁发者需要完成哪些验证步骤才能获得该证书。通过演示或源代码可以看出，经过验证的证书会在相关内容上显示出来，而且与普通的透明度标签有明显的区别。 |

| **+1pt  +1 分** | **Analytics Dashboard  分析仪表板** |
| --- | --- |
|  | Demo or source shows a view with at least 3 metrics: detection pattern (e.g., ratio of AI vs. human verdicts), appeal rate, and one additional metric of the student's choosing.  
演示或源代码中至少应包含三项指标：检测结果的比例（例如，人工智能的判断结果与人类判断结果的比例）、申诉率，以及学生自行选择的一项额外指标。 |

| **+1pt  +1 分** | **Multi-Modal Support  多模态支持** |
| --- | --- |
|  | Demo or source shows a non-text content type (e.g., image description or structured metadata) being processed through the attribution pipeline and returning a result. README describes how the pipeline handles the second content type and what signals are used for it.  
演示或源代码显示：非文本类型的内容（例如图片描述或结构化元数据）也会经过该处理流程的处理，并最终得到相应的处理结果。README 文件则说明了该处理流程是如何处理第二种类型的内容的，以及使用了哪些信号来进行处理。 |

***

### [](https://courses.codepath.org/courses/ai201/pages/grading#heading-project-5-mixtape-bug-hunt)Project 5: Mixtape Bug Hunt  
项目 5：混音带寻宝游戏

Total Points: **25pts** + 3pts bonus  
总积分：25 分 + 3 分奖励分

Required Features  所需功能

| **3pts  3 分** | **Codebase Map  代码库结构图** |
| --- | --- |
| 1 | Map identifies at least the main files and their roles — not just file names, but what each one does.  
该地图至少标明了各个主要文件及其功能——不仅仅是文件的名称，还包括每个文件的具体作用。 |
| 1 | Map describes the data flow for at least one feature (e.g., how sharing a song triggers a notification, or how the feed is populated).  
该图表描述了至少某个功能的数据流情况（例如，分享歌曲时如何触发通知，或者信息流是如何生成的）。 |
| 1 | Map reads as if it was written before bug work — it describes the app's architecture, not the bugs.  
这张图表看起来像是是在解决各种漏洞之前制作的——它描述的是应用程序的架构，而非其中的漏洞。 |

| **4pts  4 分** | **Bug Fix Completeness  漏洞修复的完整性** |
| --- | --- |
| 2 | 3 or more root cause analysis entries are present, each covering all 5 required fields: reproduction steps, navigation strategy, root cause explanation, fix description, and side-effect check.  
有 3 条或更多条根本原因分析记录，每条记录都包含了所有 5 个必填字段：问题重现步骤、操作流程、根本原因说明、解决方案描述以及潜在副作用的说明。 |
| 1 | Each entry is substantive — a grader who hasn't seen the codebase could understand what went wrong and why from reading the entry alone.  
每条记录都包含详细的信息——即使没有看过代码的人，也能通过阅读这些记录来理解到底哪里出了问题，以及为什么会出现这些问题。 |
| 1 | The submission doc is organized so entries are clearly associated with specific issue numbers.  
提交文档的格式很清晰：各项内容都明确对应了具体的问题编号。 |

| **5pts  5 分** | **Root Cause Quality  根本原因分析/质量问题的根本成因** |
| --- | --- |
| 2 | At least 3 root cause explanations identify a specific condition, comparison, function, or logic error — not just "the code was wrong here" or a restatement of the bug report.  
至少有 3 种根本原因分析能够指出具体的问题所在，比如某种条件、比较操作、函数或逻辑上的错误——而不仅仅是“代码在这里出错了”这样的简单描述，或者对错误报告的重复说明而已。 |
| 2 | At least 2 explanations name a specific function or variable and explain the mechanism: why that specific thing caused the reported behavior under the specific conditions it manifested (e.g., "only on Sundays," "only for songs with multiple tags").  
至少有两种解释会明确指出某个具体的功能或变量，并解释其作用机制：也就是解释为什么在特定的条件下，正是那个因素导致了所观察到的现象（例如：“仅在周日发生”，“仅适用于带有多个标签的歌曲”）。 |
| 1 | At least one explanation demonstrates causal reasoning — it explains not just what was wrong but why the correct behavior requires something different.  
至少有一种解释体现了因果推理的思维方式——它不仅说明了哪里出了问题，还解释了为什么正确的做法需要采取不同的方式来实施。 |

| **4pts  4 分** | **Navigation Strategy  导航策略** |
| --- | --- |
| 2 | At least 3 entries describe a real navigation path: which files were looked at, what was followed (a function call, a query, a data flow), and what moment made the student confident they'd found the root cause.  
至少有 3 条记录详细描述了实际的导航路径：具体查看了哪些文件、遵循了哪些操作步骤（函数调用、查询操作、数据流处理等），以及学生何时确认自己已经找到了问题的根本原因。 |
| 2 | The strategies described reflect deliberate exploration, not a lucky first guess. The entries show the student tracing a path, not just arriving at an answer.  
所描述的策略体现了经过深思熟虑后的探索过程，而非凭运气做出的初步猜测。从这些记录可以看出，学生是在逐步探索中找到答案的，而非直接得出结果。 |

| **3pts  3 分** | **Side-Effect Check  副作用检查** |
| --- | --- |
| 2 | At least 3 entries describe a specific, deliberate check — what related functionality was looked at after the fix to confirm it wasn't affected, and why that check was sufficient.  
至少有 3 条记录详细描述了具体的检查过程：在修复问题后，究竟检查了哪些相关功能，以确保这些功能没有受到影响；同时，也说明了为什么这样的检查就足够了。 |
| 1 | At least one entry describes a check that goes beyond "the app still ran" — it identifies a specific behavior or code path that could plausibly have been affected by the fix and confirms it wasn't.  
至少有一条测试记录描述了比“应用程序能否正常运行”更详细的测试内容——它具体指出了那些可能受到该修复措施影响的操作或代码路径，进而确认这些部分实际上并未受到影响。 |

| **3pts  3 分** | **Commit History  提交历史记录** |
| --- | --- |
| 1 | Screenshot or commit history shows commits on the `bugfix/mixtape` branch (not just the original forked state).  
截图或提交历史记录显示了 `bugfix/mixtape` 分支上的所有提交记录（而不仅仅是最初分叉时的状态）。 |
| 1 | At least 3 separate commits are visible, each corresponding to one bug fix — not all fixes bundled into a single commit.  
至少有 3 次独立的提交记录，每次提交都对应着对某个错误的修复——并非所有的修复都被合并到同一次提交中。 |
| 1 | Commit messages use conventional commit format (`fix:` prefix) and are specific enough to identify which bug was fixed without reading the code.  
提交消息遵循常规的提交格式（以 `fix:` 为前缀），其描述足够详细，因此无需查看代码就能知道具体修复了哪个错误。 |

| **3pts  3 分** | **AI Usage  人工智能的应用场景** |
| --- | --- |
| 1 | Section describes at least 2 specific uses of AI tools during codebase navigation or debugging — what was asked and what the tool helped explain or trace.  
该部分应至少列举两种在代码库导航或调试过程中使用人工智能工具的具体方式——即用户提出了什么问题，以及人工智能工具又如何帮助用户理解或追踪相关问题。 |
| 1 | Section is honest about the collaboration — describes at least one instance where the student verified something the AI explained, or where the AI's output was incomplete and the student had to course-correct.  
该部分如实描述了学生与人工智能之间的协作过程：至少举了一个例子，说明学生如何验证了人工智能的解答；或者当人工智能的回答不完整时，学生如何进行修正。 |
| 1 | Descriptions are specific enough to distinguish real AI collaboration from generic statements like "I used AI to help with code."  
这些描述足够具体，有助于区分真正的 AI 辅助工作与那些笼统的表述，比如“我使用了 AI 来辅助编写代码”。 |

Stretch Features  拉伸功能

| **+1pt  +1 分** | **Fix a 4th Bug  修复第 4 个漏洞** |
| --- | --- |
|  | A complete root cause analysis entry is present for a 4th bug, covering all 5 required fields with the same quality expected of the 3 required entries. A separate commit for this fix is visible in the `git log` screenshot.  
对于第 4 个错误，也有完整的根本原因分析记录。该记录包含了所有 5 个必填字段，其质量与前面 3 个错误对应的记录相当。在 `git log` 的截图中可以看到，针对该错误的修复已经单独提交。 |

| **+1pt  +1 分** | **Fix All 5 Bugs  修复所有 5 个漏洞** |
| --- | --- |
|  | All 5 bugs have complete root cause analysis entries. 5 separate commits are visible in the `git log` screenshot. (Requires the stretch above.)  
这 5 个漏洞都经过了彻底的根本原因分析。在 `git log` 的截图中可以看到 5 个独立的提交记录。（需要使用“stretch”版本才能查看。） |

| **+1pt  +1 分** | **Regression Test  回归测试** |
| --- | --- |
|  | A test is present in the repo that would have caught at least one of the fixed bugs before it was introduced. The submission doc references the test and briefly explains what behavior it verifies and why that test would have failed against the buggy code.  
该代码库中包含了一些测试用例，这些测试本应能在那些缺陷被引入之前就将其检测出来。提交文档中提到了这些测试用例，并简要说明了它们用来验证什么行为，以及为什么在存在缺陷的代码面前，这些测试会失败。 |

***

### [](https://courses.codepath.org/courses/ai201/pages/grading#heading-project-6-cinelog)Project 6: CineLog  项目 6：CineLog 格式

Total Points: **25pts** + 3pts bonus  
总积分：25 分 + 3 分奖励分

Required Features  所需功能

| **2pts  2 分** | **Function Rename (Comment 1)  
函数重命名（注释 1）** |
| --- | --- |
| 1 | Commit history includes a commit describing the rename of `save_to_watchlist()` to `add_to_watchlist()`.  
提交历史记录中包含了一次将 `save_to_watchlist()` 重命名为 `add_to_watchlist()` 的提交操作。 |
| 1 | PR Response Doc entry for Comment 1 describes where call sites were found and how the student confirmed none were missed — not just "I renamed it."  
关于评论 1 的公关回应文件中详细说明了这些调用点的位置，以及该学生是如何确认没有遗漏任何调用点的——而不仅仅是“我重新命名了它们”而已。 |

| **3pts  3 分** | **Deduplication (Comment 2)  
去重处理（注释 2）** |
| --- | --- |
| 1 | Commit history includes a commit describing the deduplication addition.  
提交历史记录中包含了一条关于添加去重功能的提交记录。 |
| 1 | PR Response Doc explains what the deduplication logic does — a description of the check and what happens when a duplicate is detected.  
该公关回应文件详细说明了去重逻辑的运作方式——包括检测过程以及当检测到重复内容时会发生什么。 |
| 1 | PR Response Doc references the existing `add_to_collection()` pattern or otherwise shows the student looked at how the codebase handles this case before implementing their own version.  
公关回应文档中提到了现有的 `add_to_collection()` 处理方式，或者表明该学生在自行实现解决方案之前，已经研究了代码库中处理该问题的方式。 |

| **3pts  3 分** | **Missing Test (Comment 3)  缺失的测试用例（注释 3）** |
| --- | --- |
| 1 | Commit history includes a `test:` commit describing the new test.  
提交历史记录中包含了一条 `test:` 提交记录，该记录描述了新的测试内容。 |
| 1 | PR Response Doc entry describes what the test checks and which existing test it was modeled after.  
PR 响应文档会说明该测试所检测的内容，以及该测试是根据哪项现有测试而设计的。 |
| 1 | The described test targets the right case — a nonexistent `film_id` — rather than a different edge case.  
该测试针对的是正确的场景——即不存在的 `film_id` ——而非其他异常情况。 |

| **3pts  3 分** | **Default Visibility Reasoning (Comment 4)  
默认可见性推理机制（注释 4）** |
| --- | --- |
| 1 | The response takes a clear position — public, private, or a reasoned alternative — rather than hedging or deferring.  
这种回应态度明确——要么选择公共方式，要么选择私人方式，或者提出合理的替代方案——而不会采取回避或拖延的态度。 |
| 1 | The response explains what user behavior or platform value the chosen default optimizes for. Generic statements ("public is better for discovery") earn partial at best; a specific argument about CineLog's user context earns full.  
该回答说明了所选的默认设置究竟是为了优化哪种用户行为或平台价值。那些笼统的陈述（比如“公开模式更有利于内容被发现”）最多只能获得部分认可；而那些针对 CineLog 用户使用场景的具体分析则能获得完全的认可。 |
| 1 | The response acknowledges the tradeoff — what the other option would optimize for and why the student's choice is preferable in this context.  
该回应指出了其中的权衡——即另一种选择能带来什么好处，以及为什么在这种情况下，学生的选择更为合适。 |

| **4pts  4 分** | **Sort Order Decision (Comment 5)  
排序方式决定（评论 5）** |
| --- | --- |
| 1 | The response takes a clear position — date-added, alphabetical, or a reasoned third option. A well-argued case for keeping alphabetical is worth full credit.  
该回应需要明确选择一种排序方式：按添加日期排序、按字母顺序排序，或者提出第三种合理的排序方式。如果有人能充分论证为何应按字母顺序排序，那么这一观点当然值得采纳。 |
| 1 | The response explains the user behavior the chosen order optimizes for. Specific argument about how CineLog users interact with watchlists earns full.  
该回应说明了所选排序方式所优化的用户行为。关于 CineLog 用户如何与观看列表互动的详细说明也有所提及。 |
| 1 | The response directly engages with the maintainer's point ("Most users want to see what they added recently") — either agreeing with evidence, disagreeing with a counter-argument, or proposing a synthesis.  
该回应直接回应了维护者的观点：“大多数用户都想查看自己最近添加了什么内容”。回应者可以同意这一观点，也可以反驳对方的论点，或者提出自己的综合意见。 |
| 1 | The response is substantive enough that a maintainer could approve or push back on it — not a one-liner, and not passive.  
这个回复的内容足够详细，让维护者能够据此做出批准或拒绝的决策——而不是简短的回复，也不是被动的回应。 |

| **3pts  3 分** | **Rebase and Conflict Resolution (Comment 6)  
重新提交与冲突解决（评论 6）** |
| --- | --- |
| 1 | Screenshot or commit history shows no "Merge branch" commits — the history is linear.  
截图或提交历史记录中没有任何与“合并分支”相关的提交记录——整个提交历史是线性的。 |
| 1 | Commit history includes a `fix:` commit referencing the UUID update (e.g., `fix: update film IDs to UUID format after main refactor`).  
提交历史记录中包含了一条 `fix:` 提交记录，该记录涉及 UUID 的更新操作（例如 `fix: update film IDs to UUID format after main refactor` ）。 |
| 1 | PR Response Doc entry describes what conflicted (integer vs. UUID film IDs) and what changes were made to resolve it.  
公关回应文档详细说明了哪些地方存在冲突（比如电影 ID 是整数还是 UUID 格式），以及为解决这些冲突而做了哪些调整。 |

| **3pts  3 分** | **Commit History  提交历史记录** |
| --- | --- |
| 1 | Screenshot or commit history shows all commits using conventional commit format (`feat:`, `fix:`, `test:`, `docs:`).  
截图或提交历史记录均显示了所有使用常规提交格式的提交记录（ `feat:` 、 `fix:` 、 `test:` 、 `docs:` ）。 |
| 1 | Each commit message describes one logical change with a clear, imperative summary — no "fixed stuff," "more changes," or bundled commits.  
每条提交消息都清晰地描述了某一项逻辑上的变更——不会使用诸如“修复了某些问题”、“还有其他变更”之类的模糊表述，也不会将多个变更合并在一起进行提交。 |
| 1 | The history shows at least 4 separate commits reflecting the distinct changes made (rename, dedup fix, test, rebase update, etc.).  
从历史记录来看，至少有 4 次独立的提交记录，这些提交分别反映了不同的修改内容（重命名、去重处理、测试、重新合并代码等）。 |

| **4pts  4 分** | **PR Description  公关宣传描述** |
| --- | --- |
| 1 | PR description explains what the watchlist feature does in plain language — a maintainer who hasn't seen the code can understand it.  
该 PR 描述用通俗易懂的语言解释了“监视列表”功能的作用——即使是不了解代码的维护人员也能理解。 |
| 1 | Both design decisions are explicitly named: the chosen default visibility and the chosen sort order, with a one-sentence summary of each rationale.  
这两种设计决策都有明确的名称：所选的默认可见性设置以及排序方式。每种决策都有一句简短的说明来解释其背后的理由。 |
| 1 | Testing instructions are specific enough to follow — lists the steps a reviewer would take to manually confirm the feature works, not just "test the endpoint."  
测试说明非常详细，易于遵循——其中列出了审核人员为确认该功能是否正常运作而需要执行的各项步骤，而不仅仅是“测试接口”。 |
| 1 | The PR Response Doc includes an AI Usage section documenting at least one specific use of AI tools during the project, OR a brief note that AI was not used.  
该公关回应文件中必须包含关于人工智能使用的说明，具体来说，应详细记录项目中至少一次使用人工智能工具的情况；或者，如果完全没有使用人工智能，则需简单说明这一点。 |

Stretch Features  拉伸功能

| **+1pt  +1 分** | **Add `remove_from_watchlist()`  添加 `remove_from_watchlist()`** |
| --- | --- |
|  | PR Response Doc describes the implementation, including what it does when the film isn't on the watchlist and how it follows the project's existing patterns. Commit history includes a `feat:` or `fix:` commit for the function. PR Response Doc mentions a test was written for it.  
PR 响应文档详细描述了该功能的实现方式，包括当该影片不在监控列表中时，该功能会如何运作；同时，也说明了该功能是如何遵循项目现有的运作模式的。在提交历史记录中，与该功能相关的提交记录被标记为 `feat:` 或 `fix:` 。PR 响应文档还提到，已经为该功能编写了相应的测试用例。 |

| **+1pt  +1 分** | **Second Test  第二场测试赛** |
| --- | --- |
|  | Commit history includes an additional `test:` commit beyond the one required for Comment 3. PR Response Doc explains what edge case the test covers and why the student chose that case.  
提交历史记录中，除了评论 3 所要求的提交之外，还多了一次 `test:` 提交。PR 响应文档详细说明了该测试所覆盖的边缘情况，以及为什么学生会选择测试该情况。 |

| **+1pt  +1 分** | **Visibility Toggle Endpoint  
可见性切换端点** |
| --- | --- |
|  | Commit history includes a `feat:` commit describing the visibility toggle addition. PR Response Doc describes how the `public` parameter works, what the default is, and how a caller would use it.  
提交历史记录中包含了一条 `feat:` 提交记录，该记录介绍了与可见性切换功能相关的更改。在 PR 响应文档中，详细说明了 `public` 参数的用法、默认值以及如何使用该参数。 |

***

## [](https://courses.codepath.org/courses/ai201/pages/grading#heading-module-3-pathreview)Module 3: PathReview  模块 3：路径回顾

### [](https://courses.codepath.org/courses/ai201/pages/grading#heading-week-7-issue-selection)Week 7: Issue Selection  
第 7 周：议题选择

Total Points: **10pts**  总积分：10 分

Required Features  所需功能

| **2pts  2 分** | **Issue Link  问题链接** |
| --- | --- |
| 2 | A live link to a specific `pathreview` GitHub issue is included in `JOURNAL.md`. The link resolves to an individual issue page — not the issue tracker homepage.  
`JOURNAL.md` 中包含了指向特定 `pathreview` GitHub 问题的直接链接。该链接会引导用户进入该问题的详细页面，而非问题追踪器的主页。 |

| **3pts  3 分** | **Issue Fit and Selection Reasoning  
关于适配性与选择理由的问题** |
| --- | --- |
| 1 | The issue tier is acknowledged — the student references the tier label (Tier 1, 2, or 3) and it aligns with their stated skill level or comfort with the codebase.  
该等级划分确实存在——学生会明确指出自己所属的等级（1 级、2 级或 3 级），这一等级与他们所声称的技能水平或对代码库的熟悉程度是一致的。 |
| 2 | The summary or selection notes show the student reasoned about scope fit — not just "I picked one that looked interesting." A Tier 3 selection with a clear rationale earns full credit.  
总结或选课说明应体现学生对所选课程的合理思考——而不仅仅是“随便选了个看起来有趣的课程”。如果某门课程被选为第三级课程，并且有合理的选课理由，那么该选课行为就能获得满分。 |

| **3pts  3 分** | **Problem Summary Demonstrates Understanding  
问题总结：体现了理解能力** |
| --- | --- |
| 1 | The summary describes what the issue is in plain language — not a copy-paste of the issue title.  
该摘要用通俗易懂的语言描述了问题的本质——并非简单复制问题的标题而已。 |
| 1 | The summary describes what behavior is currently broken or missing.  
该摘要说明了目前有哪些功能出现故障或缺失。 |
| 1 | The summary describes what a successful fix would accomplish.  
该摘要说明了成功的解决方案能够实现的目标。 |

| **2pts  2 分** | **Forked Repo with Setup Commits  
带有设置相关提交的分支仓库** |
| --- | --- |
| 2 | The submitted link points to a personal fork of `pathreview` (not the original repo). At least one commit beyond the initial fork is visible in the commit history, confirming the student completed local setup.  
所提交的链接指向的是 `pathreview` 的私有副本版本（并非原始仓库）。在提交历史记录中，可以看到至少一次在初始复制之后的提交记录，这证实了该学生已经完成了本地环境的配置。 |

***

### [](https://courses.codepath.org/courses/ai201/pages/grading#heading-week-8-reproduction-and-planning)Week 8: Reproduction and Planning  
第 8 周：繁殖与规划

Total Points: **10pts**  总积分：10 分

Required Features  所需功能

| **2pts  2 分** | **Starter Commits  初始提交记录** |
| --- | --- |
| 1 | At least one commit documents the reproduced issue — the message or content indicates the student confirmed the issue exists in their local environment.  
至少有一条提交记录了该问题——相关消息或内容表明，该学生已确认该问题确实存在于其本地环境中。 |
| 1 | At least one commit introduces `PLAN.md`. These can be separate commits or two distinct commits — what matters is that both actions are represented.  
至少有一次提交包含了 `PLAN.md` 。这些提交可以是单独的提交，也可以是两次不同的提交——只要能记录下这两种操作即可。 |

| **4pts  4 分** | **`PLAN.md` — Content and Specificity  
`PLAN.md` — 内容与具体性** |
| --- | --- |
| 1 | `PLAN.md` identifies what needs to change — the student describes the problem in their own words and states what a correct implementation would do differently.  
`PLAN.md` 指出了需要做出改变的地方——学生用自己的话描述了问题所在，并说明了正确的解决方案会如何有所不同。 |
| 1 | `PLAN.md` names specific parts of the codebase likely involved — files, modules, or components by name, not just "I'll look at the relevant code."  
`PLAN.md` 明确指出代码库中可能涉及的具体部分——比如文件的名称、模块或组件的名称，而不仅仅是说“我会查看相关的代码”。 |
| 2 | `PLAN.md` breaks the fix into actionable sub-tasks. At least 3 distinct sub-tasks are identified. The plan reads like something a person could follow step by step — not a restatement of the issue.  
`PLAN.md` 将整个解决方案拆分成若干个可执行的子任务。至少确定了 3 个独立的子任务。该计划清晰明了，人们可以按照步骤逐一执行——而不仅仅是问题的重复描述而已。 |

| **4pts  4 分** | **Loom Walkthrough  《Loom》游戏攻略/玩法指南** |
| --- | --- |
| 2 | The video shows the reproduced issue — the student demonstrates the broken or missing behavior in the running application. The viewer can see what goes wrong.  
该视频展示了所再现的问题——学生演示了运行中的应用程序中出现的故障或异常行为。观众可以清楚地看到问题出在哪里。 |
| 2 | The video walks through the student's intended solution approach — what they plan to fix and how. The plan is specific enough that a viewer can understand the approach without reading `PLAN.md` separately. (Video must be ≤2 minutes to earn full credit on both components. A video over 2 minutes earns a maximum of 3 points.)  
该视频详细展示了学生打算采用的解决方案——他们打算解决什么问题，以及如何解决。该计划的描述十分详细，因此观众无需再单独阅读相关说明就能理解该学生的解题思路。（为了在两个评估项目中都获得满分，视频时长必须不超过 2 分钟。如果视频时长超过 2 分钟，最多只能获得 3 分。） |

***

### [](https://courses.codepath.org/courses/ai201/pages/grading#heading-week-9-pr-submission)Week 9: PR Submission  
第 9 周：公关材料提交

Total Points: **20pts**  总积分：20 分

Required Features  所需功能

| **3pts  3 分** | **PR Submitted and Ready for Review  
公关材料已提交，随时可接受审核。** |
| --- | --- |
| 3 | The PR link is live and points to a pull request on `pathreview` marked **"Ready for review"** — not a draft. The PR is open or has received maintainer activity.  
该 PR 链接已经生效，指向 `pathreview` 上的一个 Pull Request。该 Pull Request 的状态为“已准备好接受审核”，并非草稿状态。该 PR 目前处于开放状态，或者已经得到了维护人员的处理。 |

| **5pts  5 分** | **PR Template Fully and Substantively Filled In  
公关模板已完整且详细地填写完毕** |
| --- | --- |
| 2 | The PR description explains what the fix does and how it addresses the issue — a reader who hasn't seen the code can understand what changed and why.  
该技术说明详细解释了该修复措施的具体作用以及它是如何解决相关问题的。即使没有看过代码的读者，也能明白到底发生了什么变化，以及为什么需要做这样的修改。 |
| 2 | The PR description names the issue it closes (by number or link) and includes specific instructions for how to manually verify or test the change — not just "run the tests," but actionable steps a reviewer could follow.  
该 PR 描述中明确指出了其所解决的问题（通过编号或链接来标识），同时还提供了关于如何手动验证或测试该变更的具体说明——不仅仅是“运行测试”，还包括了审查人员可以实际操作的步骤。 |
| 1 | No required section of the PR template is left at placeholder text (e.g., "describe your changes here").  
在 PR 模板中，没有任何需要填写的内容被留作占位符文本（例如“在此处描述您的更改”）。 |

| **4pts  4 分** | **Contribution Standards Documented as Followed  
贡献标准如下所示/贡献标准已详细记录如下** |
| --- | --- |
| 2 | Both self-review checkboxes in `JOURNAL.md` Check-in 2 are checked: `make check` passes and `make test-unit` passes.  
在 `JOURNAL.md` 的“检查 2”中，两个自我评估选项都已被选中： `make check` 合格， `make test-unit` 也合格。 |
| 2 | The PR branch name follows `pathreview`'s naming convention — visible in the PR URL or branch header (e.g., `fix/123-short-description`).  
该 PR 分支的名称遵循了 `pathreview` 的命名规则——可以在 PR 的 URL 或分支标题中看到该名称（例如： `fix/123-short-description` ）。 |

| **4pts  4 分** | **Tests Documented  有记录的测试结果/已记录的测试过程** |
| --- | --- |
| 2 | Check-in 2 names the specific test file(s) that were created or modified.  
“Check-in 2”会列出所有被创建或修改过的测试文件。 |
| 2 | Check-in 2 describes what the tests cover — specific enough that a reader can understand what behavior is being tested. "I wrote tests for the fix" is not sufficient; "Added tests in `test_rag_pipeline.py` covering the case where no relevant chunks are retrieved" earns full credit.  
“检查 2”部分详细说明了各项测试所涵盖的内容——描述得足够具体，以便读者能够明白究竟是哪种行为正在被测试。仅仅写着“我为该修复方案编写了测试用例”是不够的；而像“在 `test_rag_pipeline.py` 中添加了测试用例，以覆盖没有检索到任何相关数据的情况”这样的描述才能得到满分。 |

| **4pts  4 分** | **Both `JOURNAL.md` Check-Ins Present and Substantive  
`JOURNAL.md` 的两次签到都有效且内容充实。** |
| --- | --- |
| 2 | Check-in 1 (mid-week) is present with substantive content: current progress names specific sub-tasks completed from `PLAN.md`, next steps describe what remains, and blockers are noted or explicitly marked as none.  
周一至周五的签到记录都包含详细的内容：会注明目前已完成的各项子任务的名称，接着会描述还有哪些任务需要完成，同时会标明那些可能阻碍任务进展的因素，或者直接说明没有此类阻碍。 |
| 2 | Check-in 2 (end of week) is present with substantive content: the PR link is included, a 1–3 sentence description of what was built is provided, the tests field is filled in, and both self-review checkboxes are present.  
第二次提交的内容相当完整：包含了公关相关链接，有 1 到 3 句话的简要描述，测试相关字段也已填写完毕，同时两个自我审查的复选框也都打上了勾。 |

***

### [](https://courses.codepath.org/courses/ai201/pages/grading#heading-week-10-reflection)Week 10: Reflection  第 10 周：反思

Total Points: **10pts**  总积分：10 分

Required Features  所需功能

| **2pts  2 分** | **Reviewer Feedback Documented  
已记录审稿人的反馈意见** |
| --- | --- |
| 1 | The checkbox for whether reviewer feedback was received is checked (either Yes or No).  
用于标记是否已收到评审者反馈的复选框已被选中（选项为“是”或“否”）。 |
| 1 | If **Yes**: the student summarizes what the reviewer commented on and describes how they responded or plan to respond. If **No**: the student notes that no review arrived. Both outcomes earn full credit — this criterion assesses documentation, not whether review came in.  
如果是：学生需要总结评审员所提出的意见，并说明自己是如何回应的或打算如何回应的。如果不是：学生则需说明没有收到任何评审意见。无论哪种情况，都能获得满分——这一评分标准着眼于学生对评审意见的记录情况，而非是否真的收到了评审意见。 |

| **5pts  5 分** | **All Five Reflection Prompts Answered  
五个反思问题都已得到解答** |
| --- | --- |
| 5 | All five prompts are answered with at least 2–3 sentences each. No prompt is left blank or at placeholder text. The five prompts: (1) What was harder than you expected? (2) What did you learn about working in a large codebase? (3) How did AI tools help — and where did they fall short? (4) What would you do differently if you started over? (5) What are you most proud of from this module?  
五个问题都得到了至少 2-3 句的回答。没有哪个问题被留空或用占位符来代替回答。这五个问题是：(1) 有什么事情比你预想的更困难？(2) 在处理大型代码库时，你学到了什么？(3) 人工智能工具起到了什么帮助作用？又有哪些不足之处？(4) 如果可以重新开始，你会做哪些不同的事情？(5) 在这个学习过程中，你最自豪的是什么？ |

| **3pts  3 分** | **Reflection Demonstrates Specificity  
反射现象体现了其特异性/反射作用体现了其独特性** |
| --- | --- |
| 3 | At least 3 of the 5 prompts include concrete details tied to the student's actual experience — referencing their specific issue, a named file or component, a particular moment in the process, a real AI interaction, or a concrete decision they made. The response could only have been written by this student about this project.  
在 5 个提示中，至少有 3 个包含了与学生实际经历相关的具体细节——比如学生所面临的具体问题、某个具体的文件或组件、流程中的某个特定环节、与 AI 的互动情况，或是学生自己做出的具体决定。这样的回答显然只有该学生才有可能写出，因为这些内容都与他/她在这个项目中的实际经历密切相关。 |