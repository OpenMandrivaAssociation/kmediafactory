%define develname %mklibname %name -d

Name:		kmediafactory
Version:	0.8.0
Release:	%mkrel 1
URL:		http://code.google.com/p/kmediafactory/
Source0:	http://kmediafactory.googlecode.com/files/%{name}-%{version}.tar.bz2
Patch0:		kmediafactory-0.8.0-r610.patch
License:	GPLv2+
Group:		Publishing
Summary:	DVD menu generator
BuildRequires:	kdelibs4-devel
BuildRequires:	fontconfig-devel
BuildRequires:	phonon-devel
BuildRequires:	gettext
BuildRequires:	zip
BuildRequires:	dvdauthor
BuildRequires:	ffmpeg
BuildRequires:	mjpegtools
BuildRequires:	libdvdread-devel
BuildRequires:	dvd-slideshow
BuildRequires:	k3b
BuildRequires:	xine-ui
BuildRequires:	ghostscript
Requires:	zip
Requires:	dvdauthor
Requires:	ffmpeg
Requires:	mjpegtools
Requires:	dvd-slideshow
Requires:	k3b
Requires:	xine-ui
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Obsoletes:      kde4-%name < 0.6.0-4
Provides:       kde4-%name = %version-%release

%description
KMediaFactory is an easy to use template based dvd authoring tool.
You can quickly create DVD menus for home videos and TV recordings
in three simple steps. 

%files -f %{name}.lang
%defattr(-,root,root)
%{_kde_bindir}/*
%{_kde_datadir}/applications/kde4/*.desktop
%{_kde_datadir}/config/*
%{_kde_datadir}/config.kcfg/*
%{_kde_datadir}/apps/kmediafactory*
%{_kde_datadir}/apps/kmfwidgets
%{_kde_datadir}/icons/*/*/*/*
%{_kde_datadir}/kde4/services/*
%{_kde_datadir}/kde4/servicetypes/*
%{_kde_datadir}/mime/packages/kmediafactory.xml
%{_kde_libdir}/kde4/*

#--------------------------------------------------------------------

%define kmediafactorykstore_major 0
%define libkmediafactorykstore %mklibname kmediafactorykstore %{kmediafactorykstore_major}

%package -n %libkmediafactorykstore
Summary:    %name library
Group:      System/Libraries
Obsoletes:  %{mklibname kde4-kmediafactory 0}

%description -n %libkmediafactorykstore
%name library.

%files -n %libkmediafactorykstore
%defattr(-,root,root,-)
%_kde_libdir/libkmediafactorykstore.so.%{kmediafactorykstore_major}*

#--------------------------------------------------------------------

%define kmf_major 0
%define libkmf %mklibname kmf %{kmf_major}

%package -n %libkmf
Summary: %name library
Group: System/Libraries
Obsoletes:  %{mklibname kde4-kmediafactory 0}

%description -n %libkmf
%name library.

%files -n %libkmf
%defattr(-,root,root,-)
%_kde_libdir/libkmf.so.%{kmf_major}*

#--------------------------------------------------------------------

%define kmediafactoryinterfaces_major 0
%define libkmediafactoryinterfaces %mklibname kmediafactoryinterfaces %{kmediafactoryinterfaces_major}

%package -n %libkmediafactoryinterfaces
Summary: %name library
Group: System/Libraries
Obsoletes:  %{mklibname kde4-kmediafactory 0}

%description -n %libkmediafactoryinterfaces
%name library.

%files -n %libkmediafactoryinterfaces
%defattr(-,root,root,-)
%_kde_libdir/libkmediafactoryinterfaces.so.%{kmediafactoryinterfaces_major}*

#--------------------------------------------------------------------

%package -n	%{develname}
Summary:	Development headers and libraries for %{name}
Group:		Development/C++
Requires:	%{libkmediafactoryinterfaces} = %{version}
Requires:       %{libkmf} = %{version}
Requires:       %{libkmediafactorykstore} = %{version}
Provides:	lib%{name}-devel = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}
Obsoletes:	%mklibname -d %name 0
Obsoletes:	%mklibname kde4-kmediafactory -d

%description -n	%{develname}
Development libraries and headers for %{name}.

%files -n %{develname}
%defattr(-,root,root)
%{_kde_includedir}/%{name}
%{_kde_libdir}/lib*.so

#--------------------------------------------------------------------

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build

desktop-file-install --vendor='' \
	--dir=%buildroot%{_kde_datadir}/applications/kde4 \
	--remove-key='Encoding' \
	--remove-category='Application' \
	--add-category='Qt;AudioVideoEditing' \
	%buildroot%{_kde_datadir}/applications/kde4/*.desktop

%find_lang %{name} --all-name --with-html

%clean
rm -rf %{buildroot}
