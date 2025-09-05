from ansys.mapdl.core import launch_mapdl

# start MAPDL and enter the pre-processing routine
mapdl = launch_mapdl()
mapdl.clear()
mapdl.prep7()

# 以直径(1, 1), (2,2) huizh绘制一个圆。 xedge1，yedge1圆的直径一个端点坐标，xedge2，yedge2圆的直径另一个端点坐标，
anum = mapdl.cyl5(xedge1=1, yedge1=1, xedge2=2, yedge2=2)
# mapdl.aplot(savefig="test_circle.jpg", show_lines=True, line_width=5, show_bounds=True, cpos="xy")
# 保存的图片名称
image = "test_circle.png"
mapdl.aplot(savefig=image,
        show_area_numbering=True,
        show_line_numbering=True,
        color_areas=True,
        show_lines=True,
        line_width=5, show_bounds=True, cpos="xy")
print(f'image: http://172.16.16.122/app/demo/ansys/5000/api/image/{image}')

# 关闭APDL会话
mapdl.finish()