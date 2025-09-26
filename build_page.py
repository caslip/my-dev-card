def main():
    # 个人信息配置
    personal_info = {
        "name": "冀立平",
        "title": "AI Engineer",
        "description": "AI Engineer passionate about MLOps and automation.",
        "skills": ["Python", "TensorFlow", "Git", "CI/CD", "Docker"],
        "projects": [
            {"name": "项目一", "url": "https://github.com/caslip/imx6ull_IoT_smarthome.git", "description": "A machine learning pipeline for automated data preprocessing"},
            {"name": "项目二", "url": "https://github.com/caslip/stm32f1_u8g2_ssd1306.git", "description": "Containerized MLOps platform with Kubernetes"}
        ],
        "contact": {
            "github": "https://github.com/caslip",
            "linkedin": "https://linkedin.com/in/yourprofile",
            "email": "359335314@qq.com"
        },
        "blog_posts": [
            {"title": "深入理解Docker容器化技术", "date": "2023-10-15", "excerpt": "探讨Docker的核心概念和实践经验...", "url": "#"},
            {"title": "Python在机器学习中的应用", "date": "2023-09-20", "excerpt": "分享Python在机器学习项目中的最佳实践...", "url": "#"},
            {"title": "CI/CD流水线自动化部署", "date": "2023-08-10", "excerpt": "如何构建高效的持续集成和持续部署流水线...", "url": "#"}
        ]
    }
    
    # HTML模板
    html_content = f"""
    <!DOCTYPE html>
    <html lang="zh-CN">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{personal_info['name']} - Tech Blog</title>
        <style>
            * {{
                margin: 0;
                padding: 0;
                box-sizing: border-box;
            }}
            
            body {{
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                line-height: 1.6;
                color: #e0e0e0;
                background: linear-gradient(135deg, #0f0c29, #302b63, #24243e);
                min-height: 100vh;
            }}
            
            .container {{
                max-width: 1200px;
                margin: 0 auto;
                padding: 40px 20px;
            }}
            
            header {{
                text-align: center;
                padding: 60px 0;
                border-bottom: 2px solid rgba(255, 255, 255, 0.1);
                margin-bottom: 60px;
            }}
            
            .profile-img {{
                width: 150px;
                height: 150px;
                border-radius: 50%;
                background: linear-gradient(45deg, #667eea, #764ba2);
                margin: 0 auto 30px;
                display: flex;
                align-items: center;
                justify-content: center;
                font-size: 60px;
                font-weight: bold;
                color: white;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.3);
            }}
            
            h1 {{
                font-size: 3em;
                margin-bottom: 10px;
                background: linear-gradient(45deg, #667eea, #764ba2);
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                text-shadow: 0 0 30px rgba(102, 126, 234, 0.5);
            }}
            
            .title {{
                font-size: 1.5em;
                color: #a0a0a0;
                margin-bottom: 20px;
                font-weight: 300;
            }}
            
            .description {{
                font-size: 1.1em;
                color: #c0c0c0;
                max-width: 600px;
                margin: 0 auto 40px;
            }}
            
            .section {{
                margin-bottom: 60px;
                background: rgba(255, 255, 255, 0.05);
                padding: 40px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                border: 1px solid rgba(255, 255, 255, 0.1);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            }}
            
            .section-title {{
                font-size: 2em;
                margin-bottom: 30px;
                color: #667eea;
                position: relative;
                padding-bottom: 15px;
            }}
            
            .section-title::after {{
                content: '';
                position: absolute;
                bottom: 0;
                left: 0;
                width: 50px;
                height: 3px;
                background: linear-gradient(45deg, #667eea, #764ba2);
            }}
            
            .skills {{
                display: flex;
                flex-wrap: wrap;
                gap: 15px;
            }}
            
            .skill {{
                background: linear-gradient(45deg, rgba(102, 126, 234, 0.2), rgba(118, 75, 162, 0.2));
                color: #ffffff;
                padding: 12px 25px;
                border-radius: 25px;
                font-size: 0.95em;
                border: 1px solid rgba(102, 126, 234, 0.3);
                transition: all 0.3s ease;
            }}
            
            .skill:hover {{
                background: linear-gradient(45deg, rgba(102, 126, 234, 0.4), rgba(118, 75, 162, 0.4));
                transform: translateY(-2px);
                box-shadow: 0 5px 15px rgba(102, 126, 234, 0.3);
            }}
            
            .projects-grid {{
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 30px;
            }}
            
            .project-card {{
                background: rgba(255, 255, 255, 0.03);
                padding: 30px;
                border-radius: 10px;
                border: 1px solid rgba(255, 255, 255, 0.1);
                transition: all 0.3s ease;
            }}
            
            .project-card:hover {{
                background: rgba(255, 255, 255, 0.08);
                transform: translateY(-5px);
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
            }}
            
            .project-title {{
                font-size: 1.3em;
                margin-bottom: 15px;
                color: #667eea;
            }}
            
            .project-description {{
                color: #b0b0b0;
                margin-bottom: 20px;
            }}
            
            .project-link {{
                color: #667eea;
                text-decoration: none;
                font-weight: 500;
                display: inline-flex;
                align-items: center;
                gap: 5px;
                transition: color 0.3s ease;
            }}
            
            .project-link:hover {{
                color: #764ba2;
            }}
            
            .blog-posts {{
                display: grid;
                gap: 30px;
            }}
            
            .blog-post {{
                background: rgba(255, 255, 255, 0.03);
                padding: 30px;
                border-radius: 10px;
                border-left: 4px solid #667eea;
                transition: all 0.3s ease;
            }}
            
            .blog-post:hover {{
                background: rgba(255, 255, 255, 0.08);
                transform: translateX(10px);
            }}
            
            .blog-post-title {{
                font-size: 1.3em;
                margin-bottom: 10px;
                color: #667eea;
            }}
            
            .blog-post-date {{
                color: #808080;
                font-size: 0.9em;
                margin-bottom: 15px;
            }}
            
            .blog-post-excerpt {{
                color: #b0b0b0;
                margin-bottom: 20px;
            }}
            
            .blog-link {{
                color: #667eea;
                text-decoration: none;
                font-weight: 500;
                display: inline-flex;
                align-items: center;
                gap: 5px;
                transition: color 0.3s ease;
            }}
            
            .blog-link:hover {{
                color: #764ba2;
            }}
            
            .contact-info {{
                display: flex;
                justify-content: center;
                gap: 40px;
                flex-wrap: wrap;
            }}
            
            .contact-item {{
                display: flex;
                flex-direction: column;
                align-items: center;
                gap: 10px;
            }}
            
            .contact-link {{
                color: #667eea;
                text-decoration: none;
                font-size: 1.1em;
                transition: color 0.3s ease;
                display: flex;
                align-items: center;
                gap: 8px;
            }}
            
            .contact-link:hover {{
                color: #764ba2;
            }}
            
            .contact-icon {{
                font-size: 1.3em;
            }}
            
            @media (max-width: 768px) {{
                h1 {{
                    font-size: 2.2em;
                }}
                
                .title {{
                    font-size: 1.2em;
                }}
                
                .section {{
                    padding: 25px;
                }}
                
                .projects-grid {{
                    grid-template-columns: 1fr;
                }}
                
                .contact-info {{
                    flex-direction: column;
                    align-items: center;
                    gap: 20px;
                }}
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <header>
                <div class="profile-img">{personal_info['name'][0]}</div>
                <h1>{personal_info['name']}</h1>
                <div class="title">{personal_info['title']}</div>
                <p class="description">{personal_info['description']}</p>
            </header>
            
            <section class="section">
                <h2 class="section-title">技能专长</h2>
                <div class="skills">
    """
    
    # 添加技能标签
    for skill in personal_info['skills']:
        html_content += f'                    <span class="skill">{skill}</span>\n'
    
    html_content += """
                </div>
            </section>
            
            <section class="section">
                <h2 class="section-title">技术项目</h2>
                <div class="projects-grid">
    """
    
    # 添加项目卡片
    for project in personal_info['projects']:
        html_content += f"""
                    <div class="project-card">
                        <h3 class="project-title">{project['name']}</h3>
                        <p class="project-description">{project['description']}</p>
                        <a href="{project['url']}" target="_blank" class="project-link">
                            查看项目 →
                        </a>
                    </div>
        """
    
    html_content += """
                </div>
            </section>
            
            <section class="section">
                <h2 class="section-title">最新博客</h2>
                <div class="blog-posts">
    """
    
    # 添加博客文章
    for post in personal_info['blog_posts']:
        html_content += f"""
                    <article class="blog-post">
                        <h3 class="blog-post-title">{post['title']}</h3>
                        <div class="blog-post-date">{post['date']}</div>
                        <p class="blog-post-excerpt">{post['excerpt']}</p>
                        <a href="{post['url']}" class="blog-link">
                            阅读更多 →
                        </a>
                    </article>
        """
    
    html_content += f"""
                </div>
            </section>
            
            <section class="section">
                <h2 class="section-title">联系方式</h2>
                <div class="contact-info">
                    <div class="contact-item">
                        <a href="{personal_info['contact']['github']}" target="_blank" class="contact-link">
                            <span class="contact-icon">📁</span>
                            GitHub
                        </a>
                    </div>
                    <div class="contact-item">
                        <a href="mailto:{personal_info['contact']['email']}" class="contact-link">
                            <span class="contact-icon">✉️</span>
                            Email
                        </a>
                    </div>
                </div>
            </section>
        </div>
    </body>
    </html>
    """
    
    # 写入文件
    with open("index.html", "w", encoding="utf-8") as f:
        f.write(html_content)
    print("Tech-style index.html generated successfully!")


if __name__ == "__main__":
    main()
