from ansys.mapdl.core import launch_mapdl

# start MAPDL and enter the pre-processing routine
mapdl = launch_mapdl()
mapdl.clear()
mapdl.prep7()

# 定义立方体的尺寸
length = 10  # m  <可变参数: 立方体长度>
width = 8    # m  <可变参数: 立方体宽度>
height = 2   # m  <可变参数: 立方体高度>
vnum = mapdl.blc5(width=width, height=length, depth=height)
# 保存的图片名称
image = "test_block.png"
mapdl.vplot(
    # savefig=image,
    show_volume_numbering=True,
        show_area_numbering=True,
        show_line_numbering=True,
        color_areas=True,
        show_lines=True,
            line_width=5, show_bounds=True)
print(f'image: http://172.16.16.122/app/demo/ansys/5000/api/image/{image}')

# 关闭APDL会话
mapdl.finish()