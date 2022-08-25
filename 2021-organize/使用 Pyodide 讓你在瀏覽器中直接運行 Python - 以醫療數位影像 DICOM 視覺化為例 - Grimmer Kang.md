---
title: 使用 Pyodide 讓你在瀏覽器中直接運行 Python - 以醫療數位影像 DICOM 視覺化為例 - Grimmer Kang
tags: PyConTW2021, 2021-organize, 2021-共筆
---

# 使用 Pyodide 讓你在瀏覽器中直接運行 Python - 以醫療數位影像 DICOM 視覺化為例 - Grimmer Kang

{%hackmd f0JLCtZCTiWo4ZBRNKd8cg %}

<iframe src="https://app.sli.do/event/gk1xvgcv" height=450 width=100%></iframe>

<iframe src="https://wall.sli.do/event/gk1xvgcv?section=0db68317-afa2-429b-b4bb-d6f64888efcd" height=450 width=100%></iframe>


> 從這裡開始共筆

投影片連結: https://slides.com/grimmer/intro_pyodide_medical_dicom_viewer
演講影片連結: https://www.youtube.com/watch?v=Wk6sePJb26o

講者於演講後有更新或勘誤投影片的部份
- p3: Comparison of visualization + parsing solutions: 增加 offload Python server CPU loading, loadin time 3s, 較原生慢 2~5 倍 -> 可用 numpy 加速補償回來)
- p10: JavaScript access Python: 增加 get object/value from pyodide.runPythonAsync last line
- p24: [typo] to Python Position argument. Correct to "to Python Keyword argument"
- p26: todo: use comlink, a web worker lib to speed up. Even if Python part only consumes some milliseconds, but it may still affect UI event update FPS. The FPS is Ok when mouse move + Python + canvas rerender. But fps obviously dropdown if Chrome console is opened (since It uses UI main thread too)

於 PyConAPAC 2021.11.20 演講的新版投影片 https://slides.com/grimmer/pyconapac_pyodide_dicom_viewer

###### tags: `PyConTW2021`