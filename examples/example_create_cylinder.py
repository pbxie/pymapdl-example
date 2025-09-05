from ansys.mapdl.core import launch_mapdl, MapdlTheme

# start MAPDL and enter the pre-processing routine
mapdl = launch_mapdl()
mapdl.clear()
mapdl.prep7()

# 以直径(1, 1), (2,2) 的圆，高为5 绘制的圆柱体。 x1，y1圆的直径一个端点坐标，x2，y2圆的直径另一个端点坐标，depth表示圆柱的高
x1, y1, x2, y2 = 1, 1, 2, 2 # 定义圆柱体的圆：直径(1, 1), (2,2) 的圆
depth = 5 # 定义圆柱体的高
anum = mapdl.cyl5(xedge1=1, yedge1=1, xedge2=2, yedge2=2, depth=5)

# 划分网格
mapdl.et(1, "SOLID187")
# 定义网格尺寸为0.075
mapdl.esize(0.075)
mapdl.vmesh("all")

# print out the mesh characteristics
print(mapdl.mesh)

my_theme = MapdlTheme()
my_theme.background = "white"
my_theme.cmap = "jet"  # colormap
my_theme.axes.show = False
my_theme.show_scalar_bar = False

grid = mapdl.mesh.grid
# make interesting scalars
scalars = grid.points[:, 2]  # z coordinates
sbar_kwargs = {"color": "black", "title": "Z Coord"}

image = "test_cylinder.png"
grid.plot(
    off_screen=True,
    # screenshot=image,
    scalars=scalars,
    show_scalar_bar=True,
    scalar_bar_args=sbar_kwargs,
    show_edges=True,
    theme=my_theme,
)
print(f'image: http://172.16.16.122/app/demo/ansys/5000/api/image/{image}')

# 关闭APDL会话
mapdl.finish()