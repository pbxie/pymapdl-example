from ansys.mapdl.core import launch_mapdl

# 创建一个APDL实例
mapdl = launch_mapdl()

mapdl.clear()
mapdl.prep7()

# 创建yi一个底部半径为3， 顶部半径为2，高度为10的圆锥体
vnum = mapdl.con4(rad1=3, rad2=1, depth=10)

# 保存的图片名称
image = "test_cone.png"
mapdl.vplot(savefig=image, show_volume_numbering=True,
        show_area_numbering=True,
        show_line_numbering=True,
        color_areas=True,
        show_lines=True,
            line_width=5, show_bounds=True)
print(f'image: http://172.16.16.122/app/demo/ansys/5000/api/image/{image}')

# 关闭APDL会话
mapdl.finish()