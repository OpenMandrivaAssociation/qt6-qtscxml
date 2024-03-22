%define beta rc2

Name:		qt6-qtscxml
Version:	6.7.0
Release:	%{?beta:0.%{beta}.}%{?snapshot:0.%{snapshot}.}1
%if 0%{?snapshot:1}
# "git archive"-d from "dev" branch of git://code.qt.io/qt/qtbase.git
Source:		qt3d-%{?snapshot:%{snapshot}}%{!?snapshot:%{version}}.tar.zst
%else
Source:		http://download.qt-project.org/%{?beta:development}%{!?beta:official}_releases/qt/%(echo %{version}|cut -d. -f1-2)/%{version}%{?beta:-%{beta}}/submodules/qtscxml-everywhere-src-%{version}%{?beta:-%{beta}}.tar.xz
%endif
Group:		System/Libraries
Summary:	Qt %{qtmajor} XML SceneGraph Library
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6DBus)
BuildRequires:	cmake(Qt6Network)
BuildRequires:	cmake(Qt6Widgets)
BuildRequires:	cmake(Qt6Xml)
BuildRequires:	cmake(Qt6Qml)
BuildRequires:	cmake(Qt6OpenGL)
BuildRequires:	cmake(Qt6OpenGLWidgets)
BuildRequires:	cmake(Qt6Concurrent)
BuildRequires:	cmake(Qt6ShaderTools)
BuildRequires:	cmake(Qt6QmlModels)
BuildRequires:	qt6-cmake
BuildRequires:	pkgconfig(zlib)
BuildRequires:	cmake(OpenGL)
BuildRequires:	pkgconfig(gl)
BuildRequires:	pkgconfig(xkbcommon)
BuildRequires:	pkgconfig(vulkan)
License:	LGPLv3/GPLv3/GPLv2

%description
Qt %{qtmajor} XML SceneGraph library

%global extra_files_Scxml \
%{_qtdir}/plugins/scxmldatamodel

%global extra_devel_files_Scxml \
%{_qtdir}/libexec/qscxmlc \
%{_qtdir}/mkspecs/features/qscxmlc.prf \

%global extra_files_ScxmlQml \
%{_qtdir}/qml/QtScxml

%global extra_devel_files_ScxmlQml \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6declarative_scxml*.cmake

%global extra_files_StateMachineQml \
%{_qtdir}/qml/QtQml/StateMachine

%global extra_devel_files_StateMachineQml \
%{_qtdir}/lib/cmake/Qt6Qml/QmlPlugins/Qt6qtqmlstatemachine*.cmake

%qt6libs Scxml ScxmlQml StateMachine StateMachineQml

%package examples
Summary:	Example code for the Qt 6 3D module
Group:		Documentation

%description examples
Example code for the Qt 6 3D module

%prep
%autosetup -p1 -n qtscxml%{!?snapshot:-everywhere-src-%{version}%{?beta:-%{beta}}}
%cmake -G Ninja \
	-DCMAKE_INSTALL_PREFIX=%{_qtdir} \
	-DQT_BUILD_EXAMPLES:BOOL=ON \
	-DQT_WILL_INSTALL:BOOL=ON \
	-DBUILD_WITH_PCH:BOOL=OFF

%build
export LD_LIBRARY_PATH="$(pwd)/build/lib:${LD_LIBRARY_PATH}"
%ninja_build -C build

%install
%ninja_install -C build
%qt6_postinstall

%files examples
%{_qtdir}/examples
