# NIBBI 博客内容中台落地手册（非程序员版）

## 一、最终架构

- `/blogs/all`：总 Pillar Page，展示搜索、内容入口、热门/最新文章和视频。
- 其他 `/blogs/{handle}`：各 Blog Collection 页面，右侧只显示本栏目的文章。
- 所有页面左侧使用同一份总栏目列表，桌面端滚动固定，手机端折叠为 `Browse all topics`。
- 栏目名称和链接只在 Shopify Navigation 中维护一次，不逐页手写。

## 二、推荐实施方式

### 第 0 步：先做备份

1. Shopify 后台进入 `Online Store → Themes`。
2. 找到当前线上主题，点击 `… → Duplicate`。
3. 所有开发都在复制主题中完成，未确认前不要发布。

### 第 1 步：建立唯一栏目源

1. 进入 `Online Store → Navigation`。
2. 新建菜单，命名为 `NIBBI Content Hub`。
3. 按以下顺序增加链接：
   - All Content → `/blogs/all`
   - Tuning & Jetting → 对应 Blog URL
   - Diagnostics → 对应 Blog URL
   - Maintenance → 对应 Blog URL
   - Carb Guides → 对应 Blog URL
   - Model Guides → 对应 Blog URL
   - Buying & Fitment → 对应 Blog URL
   - Builds & Riders → 对应 Blog URL
   - Racing & News → 对应 Blog URL
4. 保存。以后栏目调整只改这里。

### 第 2 步：建立统一 Blog 模板

1. 在复制主题中点击 `Customize`。
2. 顶部页面选择器切换到 `Blogs`，建立新模板 `nibbi-hub`。
3. 保留官网 Header 与 Footer。
4. 中间使用一个两栏容器：左栏约 260–280px，右栏占剩余宽度。
5. 左栏添加自定义 Theme Section，并选择刚创建的 `NIBBI Content Hub` 菜单。
6. 右栏保留主题原生 Blog 文章列表、分页和 SEO 标题。
7. 在手机端把左栏改为可展开的栏目按钮，不要让左栏长期占据屏幕宽度。

> 这一步需要技术同事把左栏做成一个可复用的 Liquid Theme Section。不要在每个页面复制九个文本链接，否则后续改栏目会漏改。

### 第 3 步：给所有 Blog 使用同一个模板

1. Shopify 后台进入 `Content → Blog posts → Manage blogs`。
2. 逐个打开现有 Blog。
3. 将 Theme template 统一选择为 `blog.nibbi-hub`。
4. 保存后检查每个 URL：左栏相同，右栏文章不同，当前栏目应黄色高亮。

### 第 4 步：用 PageFly 制作 `/blogs/all` Pillar 内容

1. PageFly 新建一个内容中台页面或 Published Saved Section。
2. 按原型制作 Hero、Starting Point、Library、Trending & New、YouTube 模块。
3. 如果 `/blogs/all` 是 Shopify 原生 Blog，建议把 PageFly 内容作为已发布 Section 插入 `blog.nibbi-hub` 模板，并只在 `blog.handle == 'all'` 时显示。
4. 其他 Blog 不显示完整 Pillar 模块，只显示栏目标题、简介和文章列表。
5. PageFly 仅负责右侧内容，不要再做第二套左栏。

### 第 5 步：上线前检查

- 桌面：左栏滚动固定，但不能遮挡 Header。
- 手机：栏目默认收起，可用手指展开和选择。
- 当前栏目有明确黄色选中状态。
- 所有文章卡片链接正确，没有 `#` 临时链接。
- 原有 Blog URL 不改变，避免 SEO 迁移损失。
- 分页、Canonical、面包屑和结构化数据仍由 Shopify Theme 输出。
- PageFly 隐藏模块没有继续下载超大图片，避免页面变慢。

## 三、为什么不建议“每页放一个普通 PageFly Section”

- 普通复制 Section 后续不会可靠地统一更新。
- PageFly 的整宽 Section 不会自动与 Shopify 原生文章列表组成两栏。
- 每个 Blog 单独搭建会重复维护分页、SEO、手机样式和栏目状态。
- 最稳妥的分工是：Theme Template 管公共骨架和左栏；PageFly 管 `/blogs/all` 的营销型内容模块。

## 四、需要技术团队确认的 5 项

1. 当前主题名称及 `main-blog` Section 文件名。
2. `/blogs/all` 是真实 Blog handle，还是一个 PageFly Regular Page。
3. 现有各 Blog 的准确 handle 与负责人。
4. 是否保留现有所有 URL；默认建议保留。
5. 热门内容的数据来源：人工运营排序、GA4，还是 Shopify 浏览数据。第一版建议人工排序，稳定且成本最低。

## 五、风险与成本判断

- **框架风险（中）**：Shopify 原生 Blog 彼此独立，`/blogs/all` 无法天然把多个 Blog 的文章统一分页。第一版把它定位为精选 Pillar，而不是“全部文章无限列表”。
- **扩展风险（低）**：栏目由 Navigation 驱动后，新增栏目只需新增 Blog、菜单项并分配同一模板。
- **SEO 风险（低）**：保留现有 URL 和主题原生 Blog 输出；不要为了统一页面而批量改 URL。
- **安全风险（低）**：不在 PageFly/Liquid 中写入 API Key；YouTube、客服链接只使用公开 URL。
- **维护成本（低到中）**：日常内容团队只维护文章与菜单；技术团队只在模板结构变化时介入。
