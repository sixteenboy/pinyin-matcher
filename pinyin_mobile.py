#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
拼音匹配器 - 移动端版本 (Kivy)
适用于安卓手机的拼音汉字匹配应用
"""

import csv
import os
import sys
from typing import List, Tuple

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.core.window import Window


class PinyinMatcherApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pinyin_dict = {}
        self.load_csv_data()
    
    def build(self):
        """构建应用界面"""
        # 设置窗口背景色
        Window.clearcolor = (0.95, 0.95, 0.95, 1)
        
        # 主布局
        main_layout = BoxLayout(orientation='vertical', padding=20, spacing=15)
        
        # 标题
        title = Label(
            text='拼音匹配器',
            font_size='24sp',
            size_hint_y=None,
            height='60dp',
            color=(0.2, 0.2, 0.8, 1),
            bold=True
        )
        main_layout.add_widget(title)
        
        # 输入区域布局
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='50dp', spacing=10)
        
        # 输入框
        self.text_input = TextInput(
            hint_text='请输入拼音字母...',
            multiline=False,
            font_size='18sp',
            size_hint_x=0.8
        )
        self.text_input.bind(text=self.on_text_change)
        input_layout.add_widget(self.text_input)
        
        # 清除按钮
        clear_btn = Button(
            text='清除',
            size_hint_x=0.2,
            font_size='16sp',
            background_color=(0.8, 0.3, 0.3, 1)
        )
        clear_btn.bind(on_press=self.clear_input)
        input_layout.add_widget(clear_btn)
        
        main_layout.add_widget(input_layout)
        
        # 状态标签
        self.status_label = Label(
            text=f'已加载 {len(self.pinyin_dict)} 条拼音数据',
            font_size='14sp',
            size_hint_y=None,
            height='30dp',
            color=(0.5, 0.5, 0.5, 1)
        )
        main_layout.add_widget(self.status_label)
        
        # 结果显示区域
        self.result_scroll = ScrollView()
        self.result_label = Label(
            text='请输入拼音字母来查找匹配的汉字\n\n使用说明：\n- 输入 "a" 显示所有以 a 开头的拼音\n- 输入 "ba" 显示所有以 ba 开头的拼音\n- 输入 "bao" 显示精确匹配的结果',
            text_size=(None, None),
            font_size='16sp',
            valign='top',
            color=(0.2, 0.2, 0.2, 1)
        )
        self.result_scroll.add_widget(self.result_label)
        main_layout.add_widget(self.result_scroll)
        
        # 底部按钮布局
        button_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='50dp', spacing=10)
        
        # 帮助按钮
        help_btn = Button(
            text='帮助',
            font_size='16sp',
            background_color=(0.3, 0.6, 0.8, 1)
        )
        help_btn.bind(on_press=self.show_help)
        button_layout.add_widget(help_btn)
        
        # 关于按钮
        about_btn = Button(
            text='关于',
            font_size='16sp',
            background_color=(0.6, 0.3, 0.8, 1)
        )
        about_btn.bind(on_press=self.show_about)
        button_layout.add_widget(about_btn)
        
        main_layout.add_widget(button_layout)
        
        return main_layout
    
    def load_csv_data(self):
        """加载CSV文件数据"""
        csv_files = ["拼音.csv", "拼音1.csv"]
        total_loaded = 0
        
        for csv_file in csv_files:
            # 处理打包后的文件路径
            if hasattr(sys, '_MEIPASS'):
                base_path = sys._MEIPASS
                csv_path = os.path.join(base_path, csv_file)
            else:
                csv_path = csv_file
            
            # 检查文件是否存在
            if not os.path.exists(csv_path):
                print(f"文件 {csv_file} 不存在，跳过")
                continue
            
            # 尝试不同编码读取文件
            encodings = ['utf-8', 'gbk', 'gb2312', 'big5', 'utf-8-sig']
            
            for encoding in encodings:
                try:
                    with open(csv_path, 'r', encoding=encoding, newline='') as file:
                        first_line = file.readline()
                        file.seek(0)
                        
                        # 检查是否包含中文字符
                        if any('\u4e00' <= char <= '\u9fff' for char in first_line):
                            reader = csv.reader(file)
                            file_count = 0
                            for row in reader:
                                if len(row) >= 2 and row[0].strip() and row[1].strip():
                                    pinyin = row[0].strip()
                                    hanzi = row[1].strip()
                                    
                                    # 如果拼音已存在，合并汉字内容
                                    if pinyin in self.pinyin_dict:
                                        existing_hanzi = self.pinyin_dict[pinyin]
                                        new_hanzi_list = hanzi.split('、')
                                        existing_hanzi_list = existing_hanzi.split('、')
                                        combined_hanzi = existing_hanzi_list.copy()
                                        
                                        for new_hanzi in new_hanzi_list:
                                            new_hanzi = new_hanzi.strip()
                                            if new_hanzi and new_hanzi not in existing_hanzi_list:
                                                combined_hanzi.append(new_hanzi)
                                        
                                        self.pinyin_dict[pinyin] = '、'.join(combined_hanzi)
                                    else:
                                        self.pinyin_dict[pinyin] = hanzi
                                    
                                    file_count += 1
                            
                            total_loaded += file_count
                            print(f"从 {csv_file} 加载了 {file_count} 条数据")
                            break
                            
                except (UnicodeDecodeError, FileNotFoundError):
                    continue
        
        if total_loaded == 0:
            print("无法读取CSV文件，使用示例数据")
            self.create_sample_data()
    
    def create_sample_data(self):
        """创建示例数据"""
        sample_data = {
            "ai": "爱人、矮人",
            "ba": "爸爸、霸王、水坝、酒吧、箭靶",
            "bai": "柏树、拜佛人、伍佰",
            "ban/bang": "黑板、黑斑、木棒、地磅、帮主、皇榜",
            "bao": "城堡、皮包、猎豹、电饭煲、鲍鱼、拥抱",
            "bei": "茶杯、纪念碑、棉被、贝壳、后背",
            "ben/beng": "笔记本、笨蛋",
            "bi": "钢笔、墙壁、鼻子、匕首、婢女、雪碧",
            "bian": "皮鞭、牌匾、扁（鳊）鱼、辫子",
            "biao": "手表、飞镖、镖师、标枪",
            "bie": "鳖（甲鱼）、别针、瘪三",
            "bin/bing": "士兵、烧饼、手柄、阿炳"
        }
        self.pinyin_dict = sample_data
    
    def find_matches(self, input_text: str) -> List[Tuple[str, str]]:
        """根据输入查找匹配的拼音和汉字"""
        matches = []
        input_lower = input_text.lower().strip()
        
        if not input_lower:
            return matches
        
        for pinyin, hanzi in self.pinyin_dict.items():
            # 检查整个拼音是否以输入开头
            if pinyin.lower().startswith(input_lower):
                matches.append((pinyin, hanzi))
            # 检查多音拼音的每个部分
            elif '/' in pinyin:
                parts = pinyin.split('/')
                for part in parts:
                    if part.strip().lower().startswith(input_lower):
                        matches.append((pinyin, hanzi))
                        break
        
        # 排序：先按拼音长度，再按字母顺序
        def sort_key(item):
            pinyin = item[0].lower()
            if '/' in pinyin:
                parts = pinyin.split('/')
                matching_parts = [p.strip() for p in parts if p.strip().startswith(input_lower)]
                if matching_parts:
                    pinyin = matching_parts[0]
            return (len(pinyin), pinyin)
        
        matches.sort(key=sort_key)
        return matches
    
    def on_text_change(self, instance, value):
        """输入框文本变化时的回调"""
        # 延迟处理，避免频繁更新
        Clock.unschedule(self.update_results)
        Clock.schedule_once(lambda dt: self.update_results(value), 0.3)
    
    def update_results(self, input_text):
        """更新搜索结果"""
        if not input_text.strip():
            self.result_label.text = '请输入拼音字母来查找匹配的汉字\n\n使用说明：\n- 输入 "a" 显示所有以 a 开头的拼音\n- 输入 "ba" 显示所有以 ba 开头的拼音\n- 输入 "bao" 显示精确匹配的结果'
            self.status_label.text = f'已加载 {len(self.pinyin_dict)} 条拼音数据'
            return
        
        matches = self.find_matches(input_text)
        
        if not matches:
            self.result_label.text = f'没有找到以 "{input_text}" 开头的拼音'
            self.status_label.text = '未找到匹配结果'
            return
        
        # 构建结果文本
        result_text = f'输入: {input_text}\n' + '='*30 + '\n\n'
        
        for pinyin, hanzi in matches:
            result_text += f'{pinyin}\n{hanzi}\n\n'
        
        self.result_label.text = result_text
        self.result_label.text_size = (Window.width - 40, None)
        self.status_label.text = f'找到 {len(matches)} 个匹配结果'
    
    def clear_input(self, instance):
        """清除输入框"""
        self.text_input.text = ''
        self.text_input.focus = True
    
    def show_help(self, instance):
        """显示帮助信息"""
        help_text = '''拼音匹配器使用说明

功能：
根据输入的拼音字母，逐步匹配显示对应的汉字

使用方法：
• 在输入框中输入拼音字母
• 程序会自动显示匹配的结果
• 支持逐步匹配，如：
  - 输入 'a' 显示所有以 a 开头的拼音
  - 输入 'ba' 显示所有以 ba 开头的拼音
  - 输入 'bao' 显示精确匹配的结果

特点：
• 支持多音拼音（如 ban/bang）
• 自动合并重复拼音的汉字
• 移动端优化界面'''
        
        popup = Popup(
            title='使用帮助',
            content=Label(text=help_text, text_size=(300, None)),
            size_hint=(0.8, 0.8)
        )
        popup.open()
    
    def show_about(self, instance):
        """显示关于信息"""
        about_text = '''拼音匹配器 移动版 v1.0

一个简单易用的拼音汉字匹配工具

特点：
• 支持逐步匹配
• 移动端友好界面
• 自动加载CSV数据
• 内置示例数据

开发：AI Assistant
框架：Kivy
版本：1.0'''
        
        popup = Popup(
            title='关于',
            content=Label(text=about_text, text_size=(300, None)),
            size_hint=(0.8, 0.6)
        )
        popup.open()


if __name__ == '__main__':
    PinyinMatcherApp().run()
