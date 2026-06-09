📬 Reminder: Project 1 is due by **Monday, June 8th at 12:59AM MDT**.  
📬 提醒：项目 1 的截止时间为 6 月 8 日周一，美国山区时间凌晨 12:59。

## Show What You Know: The Unofficial Guide  
展示你的实力：非官方指南

Colleges have two kinds of knowledge: the official kind (course catalogs, housing handbooks, university websites) and the real kind — the stuff students actually share with each other to survive. Rate My Professor reviews. Subreddit threads about which dining hall is worth the walk. Anonymous posts about which off-campus apartments have mold problems. Discord servers where seniors tell freshmen what professors actually want on exams.  
大学里有两种“知识”：一种是官方提供的信息（课程目录、住宿指南、大学官网上的内容）；另一种则是学生们为了顺利度过大学生活而互相分享的真实信息。比如“Rate My Professor”这个网站上的评价、关于哪个食堂值得专程前往的讨论帖、关于哪些校外公寓有霉菌问题的匿名帖子。此外，还有 Discord 上的群组，高年级学生会告诉低年级学生老师们考试时到底看重什么。

In this project, you'll build **The Unofficial Guide**: a RAG (Retrieval-Augmented Generation) system that makes this kind of student-generated knowledge searchable and answerable. A user asks a plain-language question — "Is the housing lottery actually random?" or "Which CS professor gives the most useful feedback?" — and gets a grounded, cited answer drawn from real documents you collected.  
在这个项目中，你将打造一个名为“非官方指南”的 RAG 系统。该系统能够将学生们创建的知识内容加以整理，使其可以被检索和利用。用户只需用通俗的语言提出问题——比如“住房抽奖真的是随机进行的吗？”或“哪位计算机科学教授给出的反馈最有用？”——系统就会根据你收集到的真实文档，给出有根据的、有参考依据的答案。

This is your first production AI project. More structure is provided here than in later projects — use it to build the habits (spec first, evaluate honestly, document completely) that you'll need when that structure is gone.  
这是你的第一个人工智能相关项目。与后续的项目相比，这个项目有着更为完善的架构。请充分利用这一架构来培养那些日后不可或缺的习惯：先进行详细规划，客观地评估各项方案，然后完整地记录下所有过程。

### 🎯 Goals  🎯 目标/宗旨

By completing this project, you will be able to:  
通过完成这个项目，你将能够：

-   Build an end-to-end document processing pipeline: ingestion, chunking, and embedding.  
    构建一个端到端的文档处理流程：包括数据的读取、分割成小块以及嵌入处理。
-   Set up and query a vector store for semantic search.  
    设置并查询用于语义搜索的向量存储。
-   Generate grounded responses using retrieved context.  
    利用获取到的上下文信息来生成合理的回答。
-   Design and run an evaluation framework to measure how well your system actually works.  
    设计并运行一个评估框架，以衡量该系统的实际运行效果如何。
-   Document your design decisions so someone else could understand and extend your system.  
    把你的设计决策记录下来，这样别人才能理解并进一步扩展你的系统。

  

### ✅ Features  ✅ 功能特点

#### Required Features  必备功能/必需特性

-   **Document Ingestion Pipeline:** Collect and process at least 10 documents from your chosen domain. Your pipeline must: load the raw documents, clean or preprocess them as needed (remove navigation text, ads, etc.), and produce structured text ready for chunking. Describe this process in your README.  
    文档采集流程：从您所选择的领域中收集并处理至少 10 份文档。该流程需包括：加载原始文档，根据需要对其进行清洗或预处理（删除导航文字、广告等内容），并生成可供进一步处理的结构化文本。请在 README 文件中详细描述这一流程。
    
-   **Chunking Strategy:** Split your documents into chunks using a deliberate strategy — not just "split every 500 characters." Your `planning.md` must explain your chunk size, overlap, and why those choices fit your documents. For example, review-style text may warrant smaller chunks than long-form guides.  
    分块策略：请有意识地将文档分成若干个部分——不要简单地“每 500 个字符就分割一次”。你必须明确说明每个分块的大小、各分块之间的重叠程度，以及为何这样的划分方式最适合你的文档。例如，对于评论类文本来说，较小的分块尺寸可能更合适；而对于长篇指南而言，则需要较大的分块尺寸。
    
-   **Vector Store and Semantic Search:** Embed your chunks and store them in a vector database. Given a user query, retrieve the top relevant chunks using semantic similarity search. Your README should name the embedding model you used and reflect on what tradeoffs you'd consider if you were choosing for a production system (cost, context length, multilingual support, local vs. API).  
    向量存储与语义搜索：将您的数据块进行嵌入处理后，存储在向量数据库中。当用户提出查询时，可通过语义相似性搜索来检索出最相关的结果。在 README 文件中，请明确说明所使用的嵌入模型，并探讨在构建生产级系统时需要考虑的各种权衡因素（成本、上下文长度、多语言支持能力、本地处理与 API 接口的使用等）。
    
-   **Grounded Response Generation:** Use an LLM to generate an answer to the user's query using only the retrieved chunks as context. Responses should not rely on the model's general knowledge — they should be grounded in what was retrieved. Include source attribution (which document(s) the answer draws from) in every response.  
    基于检索内容的响应生成：利用大型语言模型，仅依据检索到的信息来生成对用户问题的回答。回答不应依赖于模型所拥有的通用知识，而应完全基于检索到的内容。每个回答都应注明信息来源，即该回答源自哪份文档或哪些文档。
    
-   **Query Interface:** Build a basic interface for querying your system. This can be a simple web UI, a command-line tool, or a notebook — but it must be usable enough to demonstrate in your video without explaining how to navigate it.  
    查询接口：需要为系统的查询功能打造一个基本的用户界面。这个界面可以是简单的网页界面、命令行工具，或是笔记本型应用程序——但无论如何，其易用性必须足够高，这样在视频中无需额外解释操作方式，就能展示该功能的用法。
    
-   **Evaluation Report:** Design 5 test questions with ground-truth answers, then run your system on each and evaluate the results. For each question, your report should document: the question, the correct answer, what your system returned, which chunks were retrieved, and whether the retrieval and response were accurate, partially accurate, or inaccurate. Identify at least one failure case and explain why it happened.  
    评估报告：请设计 5 道带有正确答案的测试题，然后让系统分别回答这些题目，并对结果进行评估。对于每一道题，报告里应包含以下内容：题目内容、正确答案、系统的回答结果、系统检索到了哪些信息，以及检索和回答的准确性——是准确、部分准确还是不准确。请至少找出一个失败案例，并说明其产生的原因。
    

#### Stretch Features  拉伸功能/拉伸特性

Complete any of these for extra credit. Update your `planning.md` before starting each one.  
完成其中任意一项即可获得额外积分。在开始每项任务之前，请先更新您的 `planning.md` 账号信息。

-   **Hybrid Search:** Combine semantic search with keyword (BM25) search and compare results to semantic-only.  
    混合搜索：将语义搜索与基于关键词的搜索方式（BM25 算法）相结合，然后将得到的搜索结果与仅使用语义搜索得到的结果进行比较。
    
-   **Chunking Strategy Comparison:** Test 2+ chunking approaches on the same query set and report which performed better and why.  
    分块策略对比：在同一查询集上测试两种以上的分块方法，分析哪种方法的性能更好，以及原因何在。
    
-   **Metadata Filtering:** Allow users to filter by document source, date, or rating (e.g., only show reviews from the past year).  
    元数据筛选：允许用户根据文档的来源、日期或评分来筛选内容（例如，仅显示过去一年内的评论）。
    
-   **Conversational Memory:** Support multi-turn queries where the system remembers context from the previous question.  
    对话式记忆：支持多轮对话处理，系统能够记住上一步提问的上下文信息。
    

💡 **Hints**  💡 提示/线索

-   Collect your documents before you write any pipeline code. You'll make better chunking decisions once you've read what you're working with.  
    在编写任何代码之前，请先准备好所需的文档。只有充分了解自己所处理的内容后，才能做出更明智的代码结构划分决策。
    
-   Test retrieval before you add generation. A lot of RAG failures are retrieval failures — the LLM can't generate a good answer from bad chunks.  
    在开始生成内容之前，先进行检索测试。很多 RAG 系统出现故障，其实都是因为检索环节出了问题——大语言模型无法从质量低下的检索结果中生成有用的答案。
    
-   Your evaluation should surface a failure. If all 5 test questions come back perfect, either your test questions are too easy or your evaluation criteria are too lenient. Make it harder.  
    你的评估结果应该能反映出某些缺陷。如果 5 道测试题的得分都为满分，那要么是这些测试题太简单了，要么就是你的评估标准过于宽松。请把测试题的难度提高一些吧。
    
-   Source citations are not optional. A system that can't tell users where its answers came from isn't production-ready.  
    引用来源是不可或缺的。如果一个系统无法向用户说明其答案的来源，那它就还无法投入实际使用。
    
-   If your system hallucinates (makes up something not in the documents), that's a valuable failure to document in your README — not something to hide.  
    如果系统的输出内容是凭空编造的、与文档内容无关，那么这其实是一种有价值的“故障信息”。这类信息应该被记录在 README 文件中，而不是被隐瞒起来。
    
-   **If your documents are PDFs** (housing guides, syllabi, handbooks, etc.), use `pdfplumber` to extract text:  
    如果您的文档是 PDF 格式的（如住房指南、教学大纲、手册等），请使用 `pdfplumber` 来提取其中的文本：
    
    ```
    <span>import</span> <span>pdfplumber</span>
    <span>pdf</span> <span>=</span> <span>pdfplumber</span><span>.</span><span>open</span><span>(</span><span>"file.pdf"</span><span>)</span>
    <span>text</span> <span>=</span> <span>"</span><span>\n\n</span><span>"</span><span>.</span><span>join</span><span>(</span><span>p</span><span>.</span><span>extract_text</span><span>()</span> <span>for</span> <span>p</span> <span>in</span> <span>pdf</span><span>.</span><span>pages</span> <span>if</span> <span>p</span><span>.</span><span>extract_text</span><span>())</span>
    ```
    
    Note that `pdfplumber` does not perform OCR — scanned image-only PDFs will produce empty text. Digitally-created PDFs (anything you can select text in) work fine.  
    请注意， `pdfplumber` 不支持 OCR 功能——仅包含扫描图像的 PDF 文件将显示为空内容。而通过数字方式创建的 PDF 文件则可以正常使用（即那些可以从中选中文本的 PDF 文件）。
    

  

### 🛠️ Tools and Setup  
🛠️ 工具与设置

This project uses a free tool stack — no paid subscriptions or API credits required.  
该项目使用的是免费的工具组合——无需支付任何费用或使用 API 额度。

#### Recommended stack  推荐的技术组合/配置

| Component  组件/组成部分 | Tool  工具 | Notes  备注/说明 |
| --- | --- | --- |
| Embeddings  嵌入向量/嵌入表示 | `sentence-transformers` (`all-MiniLM-L6-v2`) | Runs locally — no API key, no rate limits  
在本地运行——无需 API 密钥，也无需遵守任何速率限制。 |
| Vector store  向量存储 | ChromaDB | Runs locally — no account needed  
在本地运行——无需注册账户 |
| LLM | Groq (`llama-3.3-70b-versatile`)  Groq ( `llama-3.3-70b-versatile` ) | Free tier — sign up at [console.groq.com](https://console.groq.com/)  
免费套餐——请访问 console.groq.com 进行注册。 |

#### Getting started  开始使用

-   **Fork** the [Unofficial Guide starter repo](https://github.com/jamjamgobambam/ai201-project1-unofficial-guide-starter), then **clone your fork** locally.  
    从“Unofficial Guide”项目的初始仓库中创建一个分支，然后将该分支克隆到本地。
    
-   **Create and activate a virtual environment** from inside your cloned repo:  
    在克隆后的代码仓库中创建并激活虚拟环境：
    
    ```
    python <span>-m</span> venv .venv
    <span>source</span> .venv/bin/activate            <span># Mac/Linux</span>
    <span>source</span> .venv/Scripts/activate        <span># Windows (Git Bash)</span>
    <span># or: .venv\Scripts\activate         # Windows (Command Prompt)</span>
    ```
    
    You should see `(.venv)` in your terminal prompt. Do this before installing anything — it keeps this project's dependencies isolated from the rest of your system.  
    你应在终端提示符中看到 `(.venv)` 。请在安装任何软件之前先执行此操作——这样就能确保该项目的各种依赖关系不会影响到系统的其他部分。
    
-   **Install dependencies** — `requirements.txt` is already in the repo:  
    安装依赖项—— `requirements.txt` 已经存在于该代码库中：
    
    ```
    pip <span>install</span> <span>-r</span> requirements.txt
    ```
    
-   **Set up your API key.** Copy `.env.example` to `.env` in your repo root:  
    请设置好您的 API 密钥。将 `.env.example` 复制到您代码仓库的根目录下的 `.env` 位置：
    
    Then replace `your_key_here` with your Groq API key. This file is already listed in `.gitignore` — never commit it. Get a free key at [console.groq.com](https://console.groq.com/) — no credit card required.  
    然后，用你的 Groq API 密钥替换 `your_key_here` 。该文件已列在 `.gitignore` 中——切勿将其提交。你可以在 console.groq.com 免费获取 API 密钥，无需信用卡。
    

  

### Milestone 1: Choose Your Domain and Collect Documents  
里程碑 1：选择域名并准备所需文件

**⏰ ~30 min  ⏰ ~30 分钟**

Before touching any code, decide what kind of student knowledge your system will make searchable and collect the raw material. Your documents are the foundation of everything — retrieval quality, chunking decisions, and evaluation design all depend on what you're actually working with. Read them before you build anything.  
在开始编写任何代码之前，先确定你的系统应该能够检索哪种类型的学生相关知识，同时收集所需的原始数据。文档是所有工作的基础——检索效果、数据分割方式以及评估标准，都取决于你所使用的原始数据。在开始编程之前，请务必先仔细阅读这些文档。

-   Choose one **domain** for your Unofficial Guide. A domain is a **topic or category of knowledge** — not a specific website. For example, "student reviews of CS professors at \[university\]" is a domain; Rate My Professors is a _source_ you'd use to gather documents within that domain. Similarly, "off-campus housing experiences" is a domain; Reddit is a source. Keeping this distinction clear will help you stay focused when collecting documents.  
    为您的“非官方指南”选择一个主题领域。所谓“主题领域”，指的是某种知识或信息类别，而不是具体的网站。例如，“\[某大学\]计算机科学专业教授的学生评价”就是一个主题领域；而“Rate My Professors”则是一个可以用来收集该领域相关资料的网站。同样地，“校外住宿体验”也是一个主题领域；Reddit 则是一个可以用来获取相关资料的网站。明确区分这些概念，有助于您在收集资料时保持专注。
    
    Strong domain options: course and professor reviews, off-campus housing, campus dining, campus survival guides, or your own campus community. For each, sources might include Rate My Professors, department subreddits, housing forums, Yelp reviews, orientation wikis, or unofficial FAQs.  
    不错的领域选择包括：对课程和教授的评价、校外住宿信息、校园餐饮情况、校园生活指南，以及与校园社区相关的内容。对于这些信息，可以参考诸如“Rate My Professors”这样的网站、各学院的论坛、住宿相关论坛、Yelp 上的评价、迎新指南等资源，当然也可以参考非官方的常见问题解答。
    
-   Identify at least 10 specific source documents, pages, or threads. Write down each source URL or file path. More sources means better coverage — aim for sources that together answer a range of different questions, not 10 pages that all say the same thing.  
    请列出至少 10 份具体的来源文件、页面或帖子。请把每份来源的 URL 或文件路径都记下来。来源越多，覆盖的范围就越广。最好选择那些能够回答不同类型问题的来源，而不是 10 页内容完全重复的页面。
    
-   Skim your documents before you do anything else. Notice how they're structured: Are they short reviews or long guides? Are the key facts concentrated in one sentence or spread across paragraphs? This will directly inform your chunking decisions in Milestone 2.  
    在采取任何行动之前，先快速浏览一下相关文件。注意一下这些文件的结构：是简短的概述，还是详细的指南？关键信息是集中在一句话里，还是分散在各个段落中？这些信息将直接影响你在第二阶段中的处理方式。
    
-   Write a 2–3 sentence summary of your domain and what makes this knowledge hard to find otherwise. You'll use this in your `planning.md` and README.  
    请用 2-3 句话总结一下你的领域内容，以及为什么这些知识很难被轻易找到。你将在 `planning.md` 和 README 中用到这段总结。
    

**📍 Checkpoint  📍 检查点**

You have at least 10 source documents identified (with URLs or file paths) and can describe in plain language what kinds of questions your system will be able to answer. If you can't describe 5 specific questions your system should handle, your domain may be too vague — narrow it down.  
您至少需要列出 10 份源文档的详细信息（包括 URL 或文件路径），同时还需要用通俗的语言来描述该系统能够回答哪些类型的问题。如果您无法具体说明系统应该处理的 5 个问题，那么您的需求可能过于模糊了——请进一步明确您的需求范围。

Make at least one commit before moving to Milestone 2.  
在进入第 2 个里程碑之前，至少要提交一次代码。

  

***

  

### Milestone 2: Write Your Spec Before Any Code  
里程碑 2：在编写任何代码之前，先完成需求规格的编写。

**⏰ ~1 hour  ⏰ ~1 小时**

Write your `planning.md` before you write a single line of pipeline code. This isn't busywork — the decisions you make here shape every implementation choice downstream, and your spec is what you'll hand to an AI tool to generate code from. A clear spec produces useful AI-generated code. A vague one produces generic code that doesn't fit your system.  
在编写任何一行代码之前，先写下你的 `planning.md` 。这并非毫无意义的繁琐步骤——你在此做出的决策会影响到后续的所有实现细节。你的需求描述其实就是你交给 AI 工具用来生成代码的依据。清晰的需求描述能生成有用的 AI 代码；而模糊的需求描述则只能生成不适合你系统的通用代码而已。

⚠️ **AI usage guardrail:** Do not ask your AI tool to fill in `planning.md` for you. Use it to understand concepts, pressure-test your decisions, and answer specific questions — not to generate the entire plan. A spec written by AI will produce a system you can't debug. Use the guiding questions and example prompts embedded in each section as starting points for those conversations.  
⚠️ 人工智能使用准则：请不要让人工智能工具来替您填写 `planning.md` 的内容。应利用人工智能来帮助理解各种概念、对决策进行评估，以及回答具体问题——而非让人工智能来制定完整的计划。由人工智能生成的方案往往难以调试。请以各部分中提供的引导性问题及示例作为对话的起点。

-   Open the `planning.md` already in your cloned repo. The section headers are pre-populated — fill them in with real content, not placeholders or "TBD."  
    请在您克隆的代码库中打开 `planning.md` 。各部分的标题都已经预先填好了——请用实际的内容来填充这些标题，不要使用占位符或“待定”之类的字样。
    
    ```
    <span>## Domain</span>
    [What domain did you choose? Why is this knowledge valuable and hard to find through official channels?]
    
    <span>## Documents</span>
    [List your specific sources: URLs, subreddit names, forum threads, or file descriptions. Aim for variety — sources that together cover different subtopics or perspectives within your domain.]
    
    <span>## Chunking Strategy</span>
    [How will you split documents into chunks? State your chunk size (in tokens or characters), overlap size, and explain why those numbers fit the structure of your documents. A review-heavy corpus warrants different chunking than a long FAQ.
    
    Guiding questions — use these to think it through before deciding:
    <span>-</span> Are your documents short reviews (1–3 sentences) or long guides (many paragraphs)? How does that affect the right chunk size?
    <span>-</span> If a key fact spans two adjacent chunks, will either chunk be retrievable on its own? What does overlap help with?
    <span>-</span> How would you know if your chunks are too small? Too large? What would bad retrieval results look like in each case?
    
    Useful AI prompts:
    <span>-</span> "Explain how chunk size affects retrieval quality for short, opinion-based reviews."
    <span>-</span> "What are the tradeoffs between chunking by paragraph vs. fixed character count for [my document type]?"
    <span>-</span> "If I use 200-character chunks for review text, what kinds of queries might this fail for?"]
    
    <span>## Retrieval Approach</span>
    [Which embedding model are you using (e.g., all-MiniLM-L6-v2 via sentence-transformers)? How many chunks will you retrieve per query (top-k)? If you were deploying this for real users and cost wasn't a constraint, what tradeoffs would you weigh in choosing a different embedding model — context length, multilingual support, accuracy on domain-specific text, latency?
    
    Guiding questions:
    <span>-</span> How many retrieved chunks is enough to give the LLM useful context? What happens if you retrieve too few? Too many?
    <span>-</span> Why does semantic search find relevant chunks even when the query doesn't share exact words with the document?
    
    Useful AI prompts:
    <span>-</span> "What are different strategies for structuring embeddings for short, opinion-based text?"
    <span>-</span> "What does top-k mean in a retrieval system, and what are the tradeoffs of setting it too high vs. too low?"]
    
    <span>## Evaluation Plan</span>
    [List your 5 test questions with their expected correct answers. Questions should be specific enough that you can judge whether the system's response is right or wrong — "What are good dining halls?" is too vague; "What do students say about wait times at the [dining hall name] during lunch?" is testable.]
    
    <span>## Anticipated Challenges</span>
    [What could go wrong? Consider: noisy or inconsistent documents, missing source attribution, off-topic retrieval, chunks that split key information across boundaries. Name at least two specific risks.]
    
    <span>## AI Tool Plan</span>
    [Which parts of the pipeline do you plan to use AI tools (Claude, Copilot, ChatGPT, etc.) to help you implement? For each part, describe what you'll give the AI as input — which sections of this planning.md, which requirements from the instructions — and what you expect it to produce. Be specific: "I'll prompt Claude with my chunking strategy section and ask it to implement the chunk_text() function" is a plan. "I'll use AI to help me code" is not.]
    ```
    
-   Draw a simple pipeline diagram and add it to your `planning.md` under a `## Architecture` header. It doesn't need to be polished — a hand-drawn sketch photographed and embedded, an ASCII diagram, or a [Mermaid diagram](https://mermaid.js.org/syntax/flowchart.html) are all fine. Your diagram should show the five stages: Document Ingestion → Chunking → Embedding + Vector Store → Retrieval → Generation. Label each stage with the tool or library you're using (e.g., "ChromaDB" on the vector store, "all-MiniLM-L6-v2" on the embedding step). You'll use this diagram as context when prompting AI tools to implement each stage.  
    请绘制一个简单的流程图，并将其添加到你的 `planning.md` 中，标题为 `## Architecture` 。无需过于精致——手绘的草图、拍照后嵌入的图片、ASCII 格式的图表或 Mermaid 格式的图表都可以。该流程图应包含五个阶段：文档导入 → 数据分割 → 数据嵌入与向量存储 → 数据检索 → 结果生成。请在每个阶段上标注所使用的工具或库的名称（例如，向量存储阶段标注为“ChromaDB”，数据嵌入阶段标注为“all-MiniLM-L6-v2”）。在向 AI 工具发出指令以执行各个阶段时，你可以参考这个流程图。
    
-   Review your evaluation plan questions — each one should have a specific, verifiable expected answer. If a question's "correct answer" is subjective, replace it with one that isn't.  
    请仔细检查您的评估问题——每个问题都应该有明确、可验证的答案。如果某个问题的“正确答案”具有主观性，请将其替换为没有主观性的问题。
    
-   Update `planning.md` before starting any stretch features later.  
    在稍后使用任何与“伸展”功能相关的功能之前，请先更新 `planning.md` 。
    

**📍 Checkpoint  📍 检查点**

`planning.md` contains all sections with substantive content, including an AI Tool Plan that names specific pipeline components you'll prompt AI to implement. Your pipeline diagram labels each stage with the tool you're using. Your evaluation plan includes 5 specific test questions, each with a clear expected answer that a grader could check a system response against.  
`planning.md` 包含了所有包含实质性内容的部分，其中包括一份人工智能工具使用计划，其中详细列出了需要让人工智能来执行的各项任务。在流程图中，每个阶段都标明了所使用的工具。评估计划则包含了 5 个具体的测试问题，每个问题都有明确的预期答案，评分人员可以据此来评估系统的响应是否准确。

Make at least one commit before moving to Milestone 3.  
在进入第 3 个里程碑之前，至少要提交一次代码。

  

***

  

### Milestone 3: Build the Document Pipeline  
里程碑 3：构建文档处理流程

**⏰ ~2–3 hours  ⏰ ~2–3 小时**

Your pipeline has two jobs: load your documents into memory and split them into chunks your embedding model can work with. Most RAG failures trace back to bad chunks — chunks that are too large dilute the relevant information, chunks that are too small lose context. Build this carefully and verify the output before moving on. Don't skip the chunk inspection step.  
你的处理流程包含两个步骤：首先将文档加载到内存中，然后把它们分割成嵌入模型能够处理的适当大小的数据块。大多数 RAG 系统的故障都是因为数据块处理不当造成的——如果数据块过大，相关信息会被稀释；如果数据块过小，则会丢失上下文信息。请务必仔细处理这两个步骤，并在继续下一步之前验证处理结果。千万不要跳过对数据块的检查步骤。

**Start simple.** If you haven't collected your documents yet, begin with plain `.txt` files rather than live web scraping. Some sources (like Rate My Professors) are difficult to scrape due to JavaScript rendering or blocked requests — you may need to copy text manually, use PDFs, or export to a structured format. This is normal and expected. Useful AI prompts if you hit scraping issues: _"What are different ways to extract text from a JavaScript-rendered website?"_ or _"How can I convert unstructured text from a forum thread into a plain text file for processing?"_  
从简单的事情做起。如果你还没有收集到所需的文档，那就先从处理普通的文本文件开始，而不是尝试直接从网页上抓取数据。有些网站（比如 Rate My Professors）由于使用了 JavaScript 来渲染页面或阻止了外部请求，因此很难被抓取。在这种情况下，你可能需要手动复制文本、使用 PDF 格式，或者将数据导出为结构化格式。这是很正常的情况。如果你在抓取数据时遇到困难，可以参考以下 AI 提示：“有哪些方法可以从使用 JavaScript 渲染的网页中提取文本？”或者“如何将论坛帖子中的非结构化文本转换为便于处理的纯文本文件？”

The 2–3 hour estimate reflects a careful, incremental process — loading, cleaning, chunking, and validating at each step. If you find yourself finishing in 20 minutes by having AI generate everything at once, you're moving too fast. Come back and verify each stage before relying on it in the next.  
2 到 3 小时的估计时间体现了这一过程需要细致、逐步地进行——包括数据的加载、清洗、分割以及各阶段的验证。如果你发现利用人工智能一次性完成所有步骤后只需 20 分钟，那说明你的操作速度太快了。请先重新检查每个步骤，确保无误后再进入下一阶段。

-   Use your `planning.md` as a prompt to an AI tool (Claude, Copilot, ChatGPT) to generate your ingestion and chunking code. Share your Documents section (what file types and sources you have), your Chunking Strategy section, and your pipeline diagram. Ask the AI to implement a script that loads your documents, cleans them, and produces chunks matching your specified chunk size and overlap. Review what it generates: does it match your spec? Does it handle the document structure you described? Correct anything that doesn't fit, and ask the AI to explain any part you don't understand.  
    请使用您的 `planning.md` 作为提示，让 AI 工具（如 Claude、Copilot、ChatGPT）来生成用于处理文档的代码。请分享您的文档信息：您拥有哪些类型的文件以及这些文件的来源是什么；同时请说明您的文档分割策略以及整个处理流程的示意图。让 AI 编写一个脚本，用于加载文档、对其进行处理，并生成符合您所指定的大小和重叠比例的文档片段。请仔细检查 AI 生成的代码是否符合您的要求。如果有什么不合适的地方，请进行修改，并让 AI 解释那些您不明白的部分。
    
-   Write a script that loads all your documents. If you're scraping from URLs, collect the raw text. If you're using local files, load them from disk. Save the raw text to a consistent format before you start cleaning.  
    编写一个脚本来加载所有的文档。如果你是从 URL 中获取数据的，请提取其中的原始文本；如果你使用的是本地文件，则从磁盘上读取这些文件。在开始处理数据之前，请将所有原始文本保存为统一的格式。
    
-   Clean each document. Remove anything that isn't the substantive content you want your system to use:  
    请整理好每份文档。删除其中所有与您希望系统使用的核心内容无关的内容。
    
    **Remove:** HTML tags, navigation menus, cookie banners, ads, footers, repeated site headers, "Read more" links, share buttons, comment counts, and any boilerplate that appears on every page.  
    需要删除的内容包括：HTML 标签、导航菜单、广告条、页脚、重复出现的网站标题、“阅读更多”链接、分享按钮、评论数量显示，以及所有在每个页面上都会出现的固定内容。
    
    **Keep:** The actual review text, opinions, ratings, descriptions, and any context needed to understand the content (e.g., the professor's name or course number in a review).  
    保留内容：包括实际的评论文本、意见、评分、描述，以及理解该内容所必需的各类信息（例如，评论中提到的教授姓名或课程编号）。
    
    After cleaning, print one document and read it. If you still see nav text, leftover HTML entities (`&amp;`, `&nbsp;`), or content that doesn't belong to your domain, clean further before continuing.  
    清理完成后，打印出一份文档并仔细阅读。如果仍然能看到导航文本、残留的 HTML 标记（如 `&amp;` 、 `&nbsp;` ），或者不属于您所在域的内容，请继续进行进一步的清理工作。
    
-   Implement your chunking strategy from `planning.md`. Your implementation should use the chunk size and overlap you specified — if you're changing those numbers, update `planning.md` to reflect why.  
    请按照 `planning.md` 中提到的方法来实施分块策略。在实施过程中，必须使用你指定的分块大小和重叠比例。如果你对这些数值进行了更改，请务必更新 `planning.md` ，以说明更改的原因。
    
-   Print 5 representative chunks and inspect them. For each, ask: does this make sense on its own? Could someone answer a question from this chunk alone, without reading what comes before or after?  
    打印出 5 个具有代表性的段落，然后仔细检查它们。对于每一个段落，都要思考：这个段落本身是否具有逻辑性？是否有人能够仅凭这个段落来回答相关问题，而无需阅读前面的或后面的内容？
    
    **Good chunk** — a complete, retrievable thought:  
    相当完整的想法——一个可以完整表达、便于被理解的念头：
    
    > "Professor Smith's exams are heavily based on lecture slides, not the textbook. Students consistently mention that attending every class is more important than doing the readings. Midterms are curved; finals are not."  
    > 史密斯教授的考试内容主要基于课堂讲义，而非教科书。学生们普遍认为，参加每一节课比阅读教材更为重要。期中考试会有分数调整，而期末考试则不会。
    
    **Bad chunk (too small)** — a fragment with no standalone meaning:  
    无效的片段（太小了）——指那些没有任何独立意义的片段：
    
    > "Professor Smith's exams are heavily"  
    > “史密斯教授的考试难度非常大。”
    
    **Bad chunk (too large)** — multiple unrelated topics merged, too diluted to match any specific query:  
    质量太差的内容——包含多个毫无关联的主题，内容过于分散，无法满足任何具体的查询需求。
    
    > \[A 600-word chunk covering a professor's teaching style, their research interests, the department's advising policies, and unrelated comments about the building's parking situation\]  
    > \[一篇 600 字的文章，内容涵盖了一位教授的教学风格、研究领域、所在系的指导政策，以及一些与学校停车场状况无关的评论\]
    
    **Bad chunk (HTML artifact)** — cleaning didn't finish:  
    有问题的代码段（HTML 格式错误）——清理操作尚未完成：
    
    > `<div class="review-body">Professor Smith&#39;s exams are`
    
-   Count your total chunks and record the number. If you have fewer than 50 chunks across 10 documents, your chunks may be too large — each chunk is covering so much ground that specific queries can't match precisely. If you have more than 2,000, your chunks may be too small — each embedding carries so little meaning that the similarity search can't distinguish signal from noise.  
    请统计所有分块的总量并记录下来。如果在 10 份文档中，分块的总数少于 50 个，那么这些分块可能过大——每个分块所涵盖的范围太广，导致特定查询无法准确匹配到相关内容。反之，如果分块总数超过 2,000 个，那么这些分块可能过小——每个分块所包含的信息量太少，导致相似性搜索无法区分有用的信息与无用的噪声。
    

**📍 Checkpoint  📍 检查点**

Print 5 random chunks. Each one should be readable, substantive, and self-contained. If you see fragments, HTML, or empty strings, debug before embedding — bad chunks cannot be fixed by tuning retrieval later.  
打印出 5 个随机生成的片段。每个片段都应具有可读性、内容完整且能够独立存在。如果发现其中有不完整的片段、HTML 代码或空字符串，请在嵌入之前进行调试——因为事后再调整获取方式已无法修复这些错误。

Common issues and how to diagnose them:  
常见问题及诊断方法：

-   **Empty chunks:** Your splitter is producing zero-length strings — add a `len(chunk) > 0` filter, or check if your documents loaded correctly.  
    空字符串：您的分割器生成了长度为零的字符串——请添加 `len(chunk) > 0` 过滤器，或检查文档是否已正确加载。
-   **HTML artifacts:** Cleaning didn't run or didn't catch all tags — print a raw document before cleaning and compare.  
    HTML 相关问题：清理过程可能没有执行完全，或者未能识别所有的标签。建议在清理之前先打印出原始文档，以便进行对比。
-   **All chunks the same length:** Your chunker is splitting mechanically without respecting content boundaries — consider whether paragraph or sentence splitting fits your documents better.  
    所有块的长度都相同：该分割工具只是机械地执行分割操作，而不考虑内容的实际结构。请考虑一下，按段落或句子来分割内容是否更符合您的文档需求。
-   **Chunks from the wrong document:** Check that your metadata (source filename) is attached correctly to each chunk.  
    来自错误文档的片段：请确保每个片段都正确地关联了相应的元数据（源文件名）。

Make at least one commit before moving to Milestone 4.  
在进入第 4 个里程碑之前，至少要提交一次代码。

  

***

  

### Milestone 4: Embed Your Chunks and Test Retrieval  
里程碑 4：将处理后的数据嵌入到系统中，并测试数据检索功能。

**⏰ ~1-2 hours  ⏰ ~1-2 小时**

Embed your chunks and load them into a vector store, then test retrieval before you layer on generation. This step is where most retrieval bugs surface — and they're far easier to debug here than after you've wired in an LLM. Don't move to Milestone 5 until retrieval is returning relevant results.  
先将处理好的数据块嵌入到向量存储中，然后再进行检索测试。大多数检索相关的错误都出现在这个阶段——而且在这个阶段进行调试要比在将大语言模型整合进来之后容易得多。在检索功能能够返回相关结果之前，千万不要进入第 5 个阶段。

-   Use your `planning.md` Retrieval Approach section and your pipeline diagram to prompt an AI tool to generate your embedding and retrieval code. Give it your diagram to establish the full architecture, then ask it to implement the embedding step (loading chunks from your ingestion pipeline, embedding with `all-MiniLM-L6-v2`, storing in ChromaDB with source metadata) and a retrieval function. If the generated code uses a ChromaDB API call or pattern you don't recognize, ask the AI to explain it — understanding what the code does is part of the exercise.  
    请利用你的 `planning.md` 检索方案以及相关的流程图，来指导 AI 工具生成所需的嵌入和检索代码。先将流程图提供给 AI 工具，以便其构建完整的系统架构。接着，让 AI 工具执行嵌入操作：从数据输入流程中读取数据块，使用 `all-MiniLM-L6-v2` 进行嵌入处理，最后将处理后的数据连同元数据一起存储到 ChromaDB 中。同时，还要让 AI 工具实现检索功能。如果生成的代码中使用了你不熟悉的 ChromaDB API 或处理方式，请让 AI 工具进行解释——理解代码的运作原理也是这项任务的一部分。
    
-   Set up your embedding model. The recommended default is `all-MiniLM-L6-v2` from `sentence-transformers` — it runs locally with no API key and no rate limits. Load it with `SentenceTransformer("all-MiniLM-L6-v2")`.  
    请设置好您的嵌入模型。建议使用 `sentence-transformers` 中的 `all-MiniLM-L6-v2` 作为默认设置——该模型可在本地运行，无需 API 密钥或遵守任何速率限制。请使用 `SentenceTransformer("all-MiniLM-L6-v2")` 来加载该模型。
    
-   Embed all your chunks and load them into ChromaDB (or your chosen vector store) along with metadata for each chunk: at minimum, the source document name and the chunk's position in that document. You'll need source metadata later for attribution.  
    将所有的数据块嵌入其中，并将它们与每个数据块的元数据一起存储到 ChromaDB 中（或你选择的向量存储系统中）。至少需要包含源文档的名称以及该数据块在文档中的位置信息。稍后，这些元数据将用于追溯数据的来源。
    
-   Write a retrieval function that accepts a query string and returns the top-k most relevant chunks along with their source information. Start with k=4 or k=5. If you retrieve too few chunks, the relevant content may not be in the set at all. If you retrieve too many, you dilute the context with loosely related material that can pull the LLM's response off-target. You'll tune this after you've seen real results.  
    编写一个检索函数，该函数接收查询字符串作为输入，然后返回最相关的 k 个内容片段及其来源信息。初始时，可取 k=4 或 k=5。如果检索到的内容片段太少，那么可能根本找不到相关的信息；而如果检索到的内容片段太多，那些关联性不强的内容会稀释整体语境，从而影响大型语言模型的回答质量。在实际使用后，可以根据实际情况调整这个数值。
    
-   Test retrieval with at least 3 of your 5 evaluation plan queries. For each, print the returned chunks and their distance scores. Ask: are these actually relevant to the question?  
    请使用你的 5 个评估查询中的至少 3 个来测试检索效果。对于每个查询，输出被检索到的内容以及相应的距离得分。请思考：这些内容真的与问题相关吗？
    
    **Good retrieval** — specific, on-topic, from the right source:  
    良好的检索效果——信息具体、与主题相关，且来自可靠的来源：
    
    > Query: "What do students say about Professor Smith's exams?" Top result: "Professor Smith's midterms are heavily curved and focus on lecture slides. Multiple reviewers mentioned that attendance matters more than the textbook." (distance: 0.18)  
    > 查询：“学生们对史密斯教授的考试有什么评价？” 最相关的结果：“史密斯教授的期中考试评分标准相当严格，而且考试内容主要基于课堂讲义。多位学生表示，出勤率比课本内容更重要。”（相似度：0.18）
    
    **Bad retrieval** — wrong topic, or right topic but from the wrong source:  
    检索结果错误——要么主题不对，要么虽然主题正确，但来源有误。
    
    > Top result: "The parking situation near the CS building has gotten worse since construction started." (distance: 0.61) _High distance score + off-topic content = retrieval failure, probably caused by chunks that are too small to carry enough semantic signal._  
    > 最佳匹配结果：“自从 CS 大楼开始施工以来，其附近的停车状况变得更糟了。”（距离：0.61）较高的距离得分加上与主题无关的内容，导致了检索失败。这很可能是因为被检索到的文本片段太短，无法传递足够的语义信息。
    
-   If retrieval is returning chunks that seem unrelated, debug before moving on:  
    如果检索到的数据相互之间毫无关联，请先进行调试，然后再继续操作。
    
    -   **Print a retrieved chunk in full** — does it actually contain relevant content, or does it just have a few words in common with your query?  
        完整打印出检索到的内容——其中是否真的包含相关的内容呢？还是说，只不过与用户的查询条件有那么几个单词是相同的而已？
    -   **Check distance scores** — scores above 0.6–0.7 indicate weak matches. If your best result has a high score, your chunks may be too short or too noisy.  
        请检查匹配度得分——如果得分低于 0.6–0.7，说明匹配效果较差。如果您的最佳匹配结果得分较高，那可能是因为您处理的文本片段太短，或者其中包含太多干扰信息。
    -   **Check chunk content** — if chunks look like fragments or HTML leftovers, the cleaning/chunking stage didn't finish correctly.  
        检查数据块的内容——如果这些数据块看起来像是碎片或 HTML 代码的残余部分，那就说明数据块的整理/分割过程没有正确完成。
    -   **Check metadata** — if results are coming from the wrong source, verify that each chunk was stored with the correct source filename in its metadata.  
        检查元数据——如果结果来自错误的来源，请确认每个数据块的元数据中都包含了正确的源文件名。
    -   **Adjust chunk size** — if retrieval consistently pulls loosely related content, try larger chunks that carry more semantic context per embedding.  
        调整数据块大小——如果检索结果中总是包含一些关联性不强的内容，可以尝试使用更大的数据块，这样每个数据块所包含的语义信息就会更丰富。
    

**📍 Checkpoint  📍 检查点**

Querying your vector store with 3 of your test questions returns chunks that visibly relate to each question. You can point to a returned chunk and explain why it's relevant to the query. Distance scores on your top results are below 0.5. If retrieval doesn't feel right, this is the time to fix it — generation won't compensate for poor retrieval.  
用你的 3 个测试问题来查询向量存储后，得到的结果与每个问题都明显相关。你可以指着某个结果，解释为什么它与查询内容相关。排名靠前的结果的相似度得分都低于 0.5。如果检索结果不符合预期，现在就是进行修正的时候了——因为再好的生成结果也无法弥补糟糕的检索效果。

Make at least one commit before moving to Milestone 5.  
在进入第 5 个里程碑之前，至少要提交一次代码。

  

***

  

### Milestone 5: Wire Up Generation and Build Your Interface  
里程碑 5：连接各个组件并构建用户界面

**⏰ ~1-2 hours  ⏰ ~1-2 小时**

Connect retrieval to an LLM to generate grounded answers, then build a usable interface. The key engineering challenge here is grounding: your prompt must instruct the LLM to answer from the retrieved context only — not from its general training knowledge. Without this, your system will produce confident-sounding answers that have nothing to do with your documents.  
将检索结果与大型语言模型相结合，从而生成有根据的答案，然后再构建一个用户友好的界面。这里的重点在于如何正确引导大型语言模型的回答方式：必须明确指示模型仅根据检索到的信息来回答，而不能依赖其先前的训练知识。否则，系统虽然会给出看似合理的答案，但实际上这些答案与用户提供的文档内容毫无关联。

-   Use your `planning.md` and pipeline diagram to prompt an AI tool to generate the generation and interface code. Your prompt should include: your grounding requirement (answers from retrieved context only, with source attribution), the output format you want (answer + source list), and the Gradio skeleton structure if you're using it. Ask the AI to wire it all together. Before running the generated code, read through it — make sure the system prompt actually enforces grounding, not just suggests it, and that source attribution is programmatically guaranteed rather than left to the LLM to add on its own.  
    使用你的 `planning.md` 和流程图来指导 AI 工具生成相应的代码和界面。在你的指令中，应明确说明以下内容：对答案的要求（只能从已获取的上下文中获取答案，并需标注出来源）、你希望的输出格式（答案+来源列表），以及如果你使用了 Gradio 框架，还需说明其框架结构。让 AI 负责将所有部分整合在一起。在运行生成的代码之前，请务必仔细检查——确保系统确实能遵守上述要求，而不仅仅是形式上的遵守；同时，确保来源的标注是经过程序自动处理的，而不是由 LLM 自行添加的。
    
-   Connect to your LLM. The recommended default is Groq's `llama-3.3-70b-versatile`, which is free-tier and OpenAI-compatible — initialize it with `from groq import Groq` and your `GROQ_API_KEY` from `.env`. Write a prompt template that passes the retrieved chunks as context and explicitly instructs the model to answer only from that context. Example: _"Answer the question using only the information in the provided documents. If the documents don't contain enough information to answer, say 'I don't have enough information on that.'"_  
    连接到你的大型语言模型。推荐的默认选项是 Groq 的 `llama-3.3-70b-versatile` ，该模型属于免费套餐，同时兼容 OpenAI。请使用 `from groq import Groq` 以及来自 `.env` 的 `GROQ_API_KEY` 来初始化该模型。你需要编写一个提示词模板，将该模型获取到的信息作为上下文传递给模型，并明确指示模型仅基于该上下文来回答问题。例如：“请仅使用所提供的文档中的信息来回答问题。如果文档中的信息不足以回答该问题，请回复‘我无法提供足够的答案’。”
    
-   Add source attribution to your response format. The LLM's response should name which document(s) the answer came from — either by instructing the model to cite sources in its response, or by appending retrieved source names programmatically after generation.  
    在回答中必须注明信息来源。大语言模型的回答应明确指出答案源自哪份文档——要么在模型生成答案时要求其注明出处，要么在答案生成后手动添加相关文档的名称。
    
-   Test grounded generation end-to-end on 2–3 queries. The test: could this response have come from anywhere other than your retrieved chunks? If yes, it's a grounding failure — even if the answer happens to be correct.  
    通过 2 到 3 个查询来测试“端到端接地”功能是否正常。测试的内容是：这个回答是否有可能来自你获取到的数据之外的其他来源？如果是这样，那就属于“接地”失败——即便答案本身是正确的。
    
    **Grounded response** — answer traceable to retrieved text, source cited:  
    基于原文的回答——答案可追溯到所引用的文本，已注明出处：
    
    > "According to student reviews of Professor Smith (source: rmp\_smith\_reviews.txt), exams are heavily curved and focus on lecture material rather than the textbook. Several reviewers specifically recommend attending every class."  
    > 根据学生对史密斯教授的评价（来源：rmp\_smith\_reviews.txt），考试的成绩评定标准相当严格，而且考试内容主要围绕课堂讲授的内容，而非教科书。几位评价者特别建议学生务必参加每一节课。
    
    **Non-grounded response** — draws on LLM training knowledge, no citation:  
    非基于实地的回答——利用大语言模型的训练成果来生成，不引用任何参考文献：
    
    > "Professor Smith likely structures exams similarly to most CS professors, emphasizing core concepts and problem-solving skills. It's generally a good idea to review lecture notes and practice past exams for any upper-division course."  
    > “史密斯教授出题的方式，应该和大多数计算机科学专业的教授类似，会着重考查核心概念和解决问题的能力。对于任何高年级的课程来说，复习课堂笔记并练习过去的考试题目都是不错的做法。”
    
    The second response sounds authoritative and may even be correct — but it came from the model's training data, not your documents. If your system returns this kind of response, your grounding instruction needs tightening.  
    第二个回答听起来很有权威性，甚至可能是正确的——但它的依据是模型的训练数据，而非你的文档内容。如果系统总是给出这样的回答，那么你需要重新调整相关的设置或指令。
    
    Also ask a question your documents don't cover. The system should explicitly say it doesn't have enough information — not generate a plausible-sounding answer from general knowledge.  
    另外，也可以提出一些文档中没有涉及的问题。系统应该明确说明自己缺乏足够的信息，而不是凭空编造一些看似合理的答案。
    
-   Build your query interface. The recommended approach is a Gradio web UI — add `gradio>=6.9.0` to your `requirements.txt`, then `pip install gradio`. A minimal working interface looks like this:  
    构建你的查询界面。推荐的做法是使用 Gradio 网页界面——将 `gradio>=6.9.0` 添加到 `requirements.txt` 中，然后再添加 `pip install gradio` 。一个最基本的可用界面如下所示：
    
    ```
    <span>import</span> <span>gradio</span> <span>as</span> <span>gr</span>
    <span>from</span> <span>query</span> <span>import</span> <span>ask</span>  <span># or wherever your end-to-end function lives
    </span>
    <span>def</span> <span>handle_query</span><span>(</span><span>question</span><span>):</span>
        <span>result</span> <span>=</span> <span>ask</span><span>(</span><span>question</span><span>)</span>
        <span>sources</span> <span>=</span> <span>"</span><span>\n</span><span>"</span><span>.</span><span>join</span><span>(</span><span>f</span><span>"• </span><span>{</span><span>s</span><span>}</span><span>"</span> <span>for</span> <span>s</span> <span>in</span> <span>result</span><span>[</span><span>"sources"</span><span>])</span>
        <span>return</span> <span>result</span><span>[</span><span>"answer"</span><span>],</span> <span>sources</span>
    
    <span>with</span> <span>gr</span><span>.</span><span>Blocks</span><span>()</span> <span>as</span> <span>demo</span><span>:</span>
        <span>inp</span> <span>=</span> <span>gr</span><span>.</span><span>Textbox</span><span>(</span><span>label</span><span>=</span><span>"Your question"</span><span>)</span>
        <span>btn</span> <span>=</span> <span>gr</span><span>.</span><span>Button</span><span>(</span><span>"Ask"</span><span>)</span>
        <span>answer</span> <span>=</span> <span>gr</span><span>.</span><span>Textbox</span><span>(</span><span>label</span><span>=</span><span>"Answer"</span><span>,</span> <span>lines</span><span>=</span><span>8</span><span>)</span>
        <span>sources</span> <span>=</span> <span>gr</span><span>.</span><span>Textbox</span><span>(</span><span>label</span><span>=</span><span>"Retrieved from"</span><span>,</span> <span>lines</span><span>=</span><span>4</span><span>)</span>
        <span>btn</span><span>.</span><span>click</span><span>(</span><span>handle_query</span><span>,</span> <span>inputs</span><span>=</span><span>inp</span><span>,</span> <span>outputs</span><span>=</span><span>[</span><span>answer</span><span>,</span> <span>sources</span><span>])</span>
        <span>inp</span><span>.</span><span>submit</span><span>(</span><span>handle_query</span><span>,</span> <span>inputs</span><span>=</span><span>inp</span><span>,</span> <span>outputs</span><span>=</span><span>[</span><span>answer</span><span>,</span> <span>sources</span><span>])</span>
    
    <span>demo</span><span>.</span><span>launch</span><span>()</span>
    ```
    
    Run it with `python app.py` and open `http://localhost:7860`. You can also use Streamlit or a simple CLI — the requirement is that a viewer can understand how to use it from your demo video without narration explaining basic operation.  
    使用 `python app.py` 来运行它，并打开 `http://localhost:7860` 。你也可以使用 Streamlit 或简单的命令行界面来操作它。只要通过演示视频，让观众能够理解如何使用该工具即可，无需额外的操作说明。
    

**📍 Checkpoint  📍 检查点**

End-to-end: you enter a query, the system retrieves relevant chunks, and the response cites which document(s) it drew from. When you ask something your documents don't cover, the system declines to answer rather than generating something plausible but unfounded. Your interface is navigable without explanation.  
端到端处理：用户输入查询后，系统会检索出相关的信息片段，并明确指出这些信息来自哪份文档。如果用户的查询超出了文档的覆盖范围，系统会直接拒绝回答，而不会试图给出看似合理但实际上毫无根据的回答。该系统的界面非常易于使用，无需任何解释。

Make at least one commit before moving to Milestone 6.  
在进入第 6 个里程碑之前，至少要提交一次代码。

  

***

  

### Milestone 6: Evaluate, Document, and Record  
里程碑 6：评估、记录与归档

**⏰ ~1.5–2 hours  ⏰ ~1.5–2 小时**

Run your evaluation plan, write your README, and record your demo. This is where your work becomes submittable — and where the hardest intellectual work happens. Identifying and honestly explaining a failure case is more valuable than having a system that appears to work perfectly. Graders are looking for evidence that you understand your system's limitations, not just that it runs.  
执行你的评估计划，编写相关的说明文档，并录制演示视频。只有完成了这些步骤，你的作品才能被提交上去——而这也是需要付出最多脑力劳动的环节。能够准确识别并合理解释系统中的缺陷，比拥有一个看似完美的系统更为重要。评分者希望看到的是你了解自己所开发系统的局限性，而不仅仅是确认该系统能够正常运行而已。

-   Run your system on all 5 test questions from `planning.md`. For each question, record in your README: the question, the expected answer, the system's actual response, and your accuracy judgment: **accurate**, **partially accurate**, or **inaccurate**.  
    请用 `planning.md` 提供的 5 道测试题来测试你的系统。对于每一道题，你需要在 README 文件中记录以下内容：题目内容、预期答案、系统的实际回答，以及你的判断：准确、部分准确或错误。
    
-   Identify at least one failure case — a question where retrieval or generation didn't work as expected. Write a specific explanation of _why_ it failed, tied to a part of the pipeline. "The answer was wrong" is not an explanation. "The relevant information was split across a chunk boundary, so the retrieval returned only half the context" or "The embedding model treated the professor's nickname as an out-of-vocabulary token and returned unrelated results" are explanations.  
    请至少举出一个失败案例——也就是那些检索或生成结果不符合预期的情况。请详细解释为什么会出现这种失败情况，並指出是流程中的哪个环节出了问题。“答案错了”不算是一种有效的解释。而“相关信息被分割在了不同的数据块之间，因此检索到的只是部分信息”或“嵌入模型将教授的昵称视为无效输入，从而得到了无关的结果”，这些才算是有效的解释。
    
-   Complete your `README.md` using the template already in the starter repo. Every section has a guiding prompt — replace the prompts with your actual content. Every section is required; one-liners will not receive full credit.  
    请使用启动包中的模板来完成您的 `README.md` 内容。每个部分都有相应的提示语——请用您自己的内容来替换这些提示语。所有部分都是必填的；只有完整的句子才能获得满分。
    
-   Write your spec reflection in the README: describe one way the spec helped guide your implementation and one way your implementation diverged from it and why.  
    请在 README 文件中写下对相关规范的思考：说明该规范在指导你的实现过程中起到了怎样的作用；同时，说明你的实现与该规范有哪些不同之处，以及原因何在。
    
-   Add the AI usage section to your README. Describe at least 2 specific instances: what you asked the AI tool to do, what it produced, and what you changed, overrode, or directed differently.  
    在 README 文件中加入关于 AI 使用情况的描述。请至少列举两个具体例子：你让 AI 工具完成了什么任务，它产生了什么结果，以及你对这些结果做了哪些修改或调整。
    
-   Record a 3–5 minute demo video. Show: at least 3 different queries with source citations visible in the response, one query where retrieval and generation both work well, one query where the system struggles or fails (narrate what went wrong), and a brief walkthrough of your evaluation report.  
    请录制一段 3 到 5 分钟的演示视频。视频中需包含：至少 3 个不同的查询示例，且每个示例的响应中都应显示相关的来源信息；其中一个查询的检索和生成功能都表现良好；另一个查询则应展示系统出现的问题或失败的情况（请详细说明问题所在）；最后，请简要介绍一下您的评估报告内容。
    

**📍 Checkpoint  📍 检查点**

All 5 evaluation questions are documented with accuracy judgments in your README. At least one failure is explained with a specific cause tied to the pipeline. README covers all required sections. Demo video is recorded and shows all required moments.  
在 README 文件中，所有 5 个评估问题都附有详细的判断结果。对于每一个失败案例，都详细说明了导致失败的具体原因。README 文件涵盖了所有必要的内容。演示视频也已录制完成，展示了所有必要的环节。

Make a final commit with your completed README and evaluation results before submitting.  
在提交之前，请确保已经完成了 README 文件的编写以及各项评估结果的整理，然后进行最后的提交操作。

  

***

  

### 📬 Submitting Your Project  
📬 提交您的项目

Submit all of the following through the Course Portal:  
请通过课程门户提交以下所有内容：

-   Link to your forked GitHub repository  
    请提供您在 GitHub 上创建的分支仓库的链接。
    
-   `planning.md` in your repo root (written before implementation, updated before stretch features)  
    `planning.md` 位于你的代码仓库的根目录中（在代码实现之前编写，会在 Stretch 版本发布前进行更新）
    
-   `README.md` including:    `README.md` 包括：
    
    -   Domain and document sources (with specific names/URLs)  
        域名和文档来源（包括具体的名称/网址）
    -   Chunking strategy and reasoning (chunk size, overlap, why it fits your documents)  
        分块策略与推理机制（分块大小、重叠部分、为何这种分块方式适合您的文档）
    -   Sample chunks: at least 5 labeled sample chunks, each with its source document name  
        样本片段：至少 5 个带有标签的样本片段，每个样本片段都标明了其对应的源文档名称。
    -   Embedding model used, and a brief reflection on what tradeoffs you'd consider when choosing a model for a production deployment  
        所使用的嵌入模型，以及在选择用于实际部署的模型时需要考虑的各种权衡因素的简要分析。
    -   Retrieval test results: at least 3 queries, each showing the query and the top returned chunks; for at least 2 of them, a written explanation of why the returned chunks are relevant  
        检索测试结果：至少进行 3 次查询，每次查询都要显示查询内容以及查询结果中的前几条记录。其中至少 2 次查询，需要附上书面说明，解释为什么所返回的记录与查询内容相关。
    -   How grounded generation is enforced in your system (prompt design or pipeline structure)  
        在您的系统中，是如何确保“接地气”的原则得到贯彻的？是通过提示词的设计，还是通过系统的整体架构来实现的？
    -   Example responses: at least 2 responses with source attribution visible in the output text, plus one out-of-scope query showing the system's refusal response  
        示例回复：至少 2 条回复，其来源信息需在输出文本中清晰显示；另外还需包含 1 条超出系统处理范围的查询，以体现系统的拒绝回应。
    -   Query interface: a description of the input and output fields, and a sample interaction transcript showing one complete query and response  
        查询界面：包括对输入字段和输出字段的描述，以及一段示例性的交互记录，展示了一次完整的查询与响应过程。
    -   Evaluation report: all 5 test questions with expected answers, system responses, and accuracy judgments  
        评估报告：全部 5 道测试题的预期答案、系统反馈以及准确率评估结果均已记录。
    -   At least one honest failure case with a specific explanation of why it happened  
        至少要有一个关于失败情况的真实案例，并详细说明失败的原因。
    -   Spec reflection: one way the spec helped you, one way implementation diverged from it and why  
        规格说明的体现：该规格说明对您有何帮助；在实施过程中，有哪些地方与规格说明有所偏差，原因是什么。
    -   AI usage section: at least 2 specific instances describing what you directed the AI to do and what you revised or overrode  
        AI 使用情况：至少需要举两个具体例子，说明你让 AI 执行了哪些操作，以及你对 AI 的决策进行了哪些修改或否决。
    
-   Demo video (3–5 minutes) showing:  
    演示视频（3–5 分钟），内容包含：
    
    -   At least 3 different queries answered with source citations visible in the response  
        至少有 3 个不同的查询得到了回答，且回答中都附有相关的来源引用。
    -   One query where retrieval works well (briefly narrate why the retrieved chunks are relevant)  
        有一个查询的检索效果很好（简要说明为什么检索到的内容与查询相关）。
    -   One query where the system struggles or fails (narrate what went wrong)  
        系统在处理某个查询时遇到困难或无法完成该查询的情况（请详细描述出了什么问题）
    -   A walkthrough of the evaluation report  
        评估报告的详细解读/评估报告的内容详解
    

***

### 🗺️ How It's Graded  
🗺️ 评分标准是怎样的

_A detailed breakdown of graded features and points can be found on the course [grading](https://courses.codepath.org/courses/ai201/pages/grading#heading-project-1-the-unofficial-guide) page.  
关于各项评分标准及具体分数的详细信息，请查看课程评分页面。_