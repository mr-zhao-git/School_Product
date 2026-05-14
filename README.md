# 电影个性化推荐系统（Django + Vue）

## 功能
- 用户端：首页高分电影、分类筛选、个性化推荐、个人中心与导出推荐数据。
- 管理端：可视化饼图（观看数/搜索度）、评论好坏评统计、电影管理、用户管理。

## 启动
### 后端
```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

### 前端
```bash
cd frontend
npm install
npm run dev
```

## API 说明
- `/api/home/` 首页高分电影
- `/api/category/?category=科幻` 分类筛选
- `/api/recommend/?user_id=1` 个性化推荐
- `/api/hot/` 热门榜单
- `/api/ratings/` 评分录入
- `/api/favorites/?user_id=1` 我的收藏
- `/api/export/?user_id=1` 导出推荐 CSV
- `/api/dashboard/` 管理端图表和评论统计
- `/api/users/` 用户管理列表
